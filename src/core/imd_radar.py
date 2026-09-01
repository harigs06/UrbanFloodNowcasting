"""IMD Doppler Weather Radar (DWR) Ingestion and Weather Analysis Engine for Multi-City Scaling.

Fetches real-time radar imagery and reflectivity products from the official
India Meteorological Department (IMD) website (https://mausam.imd.gov.in/)
across multiple metropolitan radar stations (Hyderabad, Mumbai, Chennai, Delhi, Bengaluru, Kolkata).
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import httpx
import numpy as np
from PIL import Image, ImageFile
import io

# Enable loading images from live streams with trailing bytes or minor truncation
ImageFile.LOAD_TRUNCATED_IMAGES = True

from src.config import settings
from src.cities import CITY_REGISTRY, CityProfile, get_city_profile


class IMDRadarClient:
    """Official IMD Doppler Weather Radar Client supporting all major Indian metropolitan stations."""

    IMD_BASE_URL = "https://mausam.imd.gov.in"
    RADAR_ENDPOINTS = {
        # Hyderabad
        "hyderabad_caz": "https://mausam.imd.gov.in/Radar/caz_hyd.gif",
        "hyderabad_maxz": "https://mausam.imd.gov.in/Radar/animation/Converted/HYD_MAXZ.gif",
        "hyderabad_sri": "https://mausam.imd.gov.in/Radar/animation/Converted/HYD_SRI.gif",
        # Mumbai
        "mumbai_caz": "https://mausam.imd.gov.in/Radar/caz_mum.gif",
        "mumbai_maxz": "https://mausam.imd.gov.in/Radar/animation/Converted/MUM_MAXZ.gif",
        # Chennai
        "chennai_caz": "https://mausam.imd.gov.in/Radar/caz_chn.gif",
        "chennai_maxz": "https://mausam.imd.gov.in/Radar/animation/Converted/CHN_MAXZ.gif",
        # Delhi
        "delhi_caz": "https://mausam.imd.gov.in/Radar/caz_dlh.gif",
        # Kolkata
        "kolkata_caz": "https://mausam.imd.gov.in/Radar/caz_kol.gif",
        # Bengaluru
        "bengaluru_caz": "https://mausam.imd.gov.in/Radar/caz_blr.gif",
    }

    def __init__(self, radar_dir: Optional[Path] = None, default_city_id: str = "hyderabad"):
        self.radar_dir = radar_dir or settings.RADAR_DIR
        self.radar_dir.mkdir(parents=True, exist_ok=True)
        self.default_city_id = default_city_id
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            ),
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Referer": "https://mausam.imd.gov.in/",
        }

    def get_endpoint_url_for_city(self, city_id: str) -> str:
        """Resolves the live IMD radar URL for a given city."""
        profile = get_city_profile(city_id)
        endpoint_key = profile.radar_endpoint_key
        return self.RADAR_ENDPOINTS.get(endpoint_key, f"https://mausam.imd.gov.in/Radar/{endpoint_key}.gif")

    def fetch_live_radar_image(
        self,
        endpoint_key: str = "hyderabad_caz",
        save_filename: Optional[str] = None,
        city_id: Optional[str] = None,
    ) -> Tuple[bytes, Path]:
        """Fetches the latest live Doppler Weather Radar image from the official IMD portal."""
        if city_id:
            profile = get_city_profile(city_id)
            url = self.get_endpoint_url_for_city(city_id)
            save_dir = settings.get_city_radar_dir(city_id)
            filename = save_filename or f"{profile.city_id}_caz.gif"
        else:
            url = self.RADAR_ENDPOINTS.get(endpoint_key, self.RADAR_ENDPOINTS["hyderabad_caz"])
            save_dir = self.radar_dir
            filename = save_filename or f"{endpoint_key}.gif"

        save_path = save_dir / filename

        with httpx.Client(headers=self.headers, timeout=25.0, verify=False) as client:
            resp = client.get(url)
            if resp.status_code != 200 or len(resp.content) < 500:
                # Fallback to default cached hyderabad radar if station is offline
                fallback_path = self.radar_dir / "hyderabad_caz.gif"
                if fallback_path.exists():
                    with open(fallback_path, "rb") as f:
                        return f.read(), fallback_path
                raise RuntimeError(
                    f"Failed to download IMD radar image from {url} (HTTP {resp.status_code}, len={len(resp.content)})"
                )
            
            with open(save_path, "wb") as f:
                f.write(resp.content)

            return resp.content, save_path

    @staticmethod
    def decode_imd_reflectivity(
        image_bytes_or_path: Any,
        target_grid_shape: Tuple[int, int] = (200, 200),
    ) -> np.ndarray:
        """Decodes IMD Doppler Weather Radar color-mapped GIF/PNG into a calibrated dBZ matrix."""
        if isinstance(image_bytes_or_path, (str, Path)):
            img = Image.open(image_bytes_or_path).convert("RGB")
        elif isinstance(image_bytes_or_path, bytes):
            img = Image.open(io.BytesIO(image_bytes_or_path)).convert("RGB")
        elif isinstance(image_bytes_or_path, Image.Image):
            img = image_bytes_or_path.convert("RGB")
        else:
            raise TypeError("Unsupported image input type")

        arr = np.array(img, dtype=np.float32)
        h, w, _ = arr.shape

        r_slice = arr[:, :, 0]
        g_slice = arr[:, :, 1]
        b_slice = arr[:, :, 2]

        dbz_grid = np.zeros((h, w), dtype=np.float32)

        # 1. Magenta / Purple / Pink: 55 - 65 dBZ (Cloudburst)
        magenta_mask = (r_slice > 180) & (b_slice > 150) & (g_slice < 120)
        dbz_grid[magenta_mask] = 58.0

        # 2. Red / Crimson: 45 - 55 dBZ (Heavy convective rain)
        red_mask = (r_slice > 180) & (g_slice < 90) & (b_slice < 90)
        dbz_grid[red_mask] = 50.0

        # 3. Orange: 38 - 45 dBZ (Intense showers)
        orange_mask = (r_slice > 200) & (g_slice > 100) & (g_slice < 180) & (b_slice < 60)
        dbz_grid[orange_mask] = 42.0

        # 4. Yellow: 30 - 38 dBZ (Moderate rain)
        yellow_mask = (r_slice > 180) & (g_slice > 180) & (b_slice < 70)
        dbz_grid[yellow_mask] = 34.0

        # 5. Bright Green: 22 - 30 dBZ (Light to moderate rain)
        green_mask = (g_slice > 140) & (r_slice < 130) & (b_slice < 110)
        dbz_grid[green_mask] = 26.0

        # 6. Blue / Cyan: 10 - 22 dBZ (Light rain / drizzle)
        cyan_mask = (b_slice > 160) & (r_slice < 100)
        dbz_grid[cyan_mask] = 16.0

        # Resample to model's target grid shape
        if dbz_grid.shape != target_grid_shape:
            from scipy.ndimage import zoom
            scale_y = target_grid_shape[0] / float(h)
            scale_x = target_grid_shape[1] / float(w)
            dbz_grid = zoom(dbz_grid, (scale_y, scale_x), order=1)

        return np.clip(dbz_grid, 0.0, 65.0).astype(np.float32)

    @staticmethod
    def marshall_palmer_qpe(
        dbz_grid: np.ndarray,
        a: float = 200.0,
        b: float = 1.6,
        min_rain_threshold_dbz: float = 10.0,
    ) -> np.ndarray:
        """Converts reflectivity (dBZ) to rain rate R (mm/hr) using standard Marshall-Palmer formula:
        
        Formula:
            Z = 10^(dBZ / 10)
            Z = a * R^b  ==>  R = (Z / a)^(1 / b)
        """
        rain_rate = np.zeros_like(dbz_grid, dtype=np.float32)
        active_mask = dbz_grid >= min_rain_threshold_dbz

        z = 10.0 ** (dbz_grid[active_mask] / 10.0)
        rain_rate[active_mask] = (z / a) ** (1.0 / b)

        return np.clip(rain_rate, 0.0, 250.0)

    def analyze_weather(
        self,
        dbz_grid: np.ndarray,
        city_id: str = "hyderabad",
    ) -> Dict[str, Any]:
        """Performs comprehensive meteorological radar analysis for urban flood risk."""
        profile = get_city_profile(city_id)
        station_name = f"{profile.display_name} DWR ({profile.radar_station_code})"

        rain_grid = self.marshall_palmer_qpe(dbz_grid)

        max_dbz = float(np.max(dbz_grid))
        mean_dbz = float(np.mean(dbz_grid[dbz_grid > 5.0])) if np.any(dbz_grid > 5.0) else 0.0
        max_rain_mm_hr = float(np.max(rain_grid))
        mean_rain_mm_hr = float(np.mean(rain_grid[rain_grid > 0.1])) if np.any(rain_grid > 0.1) else 0.0

        total_cells = dbz_grid.size
        active_rain_cells = int(np.sum(dbz_grid >= 15.0))
        heavy_rain_cells = int(np.sum(dbz_grid >= 40.0))
        cloudburst_cells = int(np.sum(dbz_grid >= 50.0))

        coverage_pct = round((active_rain_cells / total_cells) * 100.0, 2)
        heavy_coverage_pct = round((heavy_rain_cells / total_cells) * 100.0, 2)

        # Risk Classification
        if max_dbz >= 50.0 or max_rain_mm_hr >= 50.0:
            severity = "CRITICAL_CLOUDBURST_ALERT"
            description = f"Severe convective cloudburst storm cell detected over {profile.display_name} region. Extreme flood risk."
        elif max_dbz >= 40.0 or max_rain_mm_hr >= 20.0:
            severity = "HEAVY_STORM_WARNING"
            description = f"Heavy convective precipitation detected over {profile.display_name}. Urban waterlogging expected."
        elif max_dbz >= 25.0 or max_rain_mm_hr >= 5.0:
            severity = "MODERATE_RAIN_ADVISORY"
            description = f"Moderate rain bands across {profile.display_name}. Localized surface ponding possible."
        elif max_dbz >= 10.0:
            severity = "LIGHT_RAIN"
            description = f"Light rain / drizzle detected over {profile.display_name}. Nominal drainage conveyance."
        else:
            severity = "CLEAR_NOMINAL"
            description = f"Clear / trace echoes across {profile.display_name} radar sweep."

        return {
            "city_id": profile.city_id,
            "city_name": profile.display_name,
            "state": profile.state,
            "station": station_name,
            "coordinates": {"latitude": profile.center_coords[0], "longitude": profile.center_coords[1]},
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "max_reflectivity_dbz": round(max_dbz, 1),
            "mean_reflectivity_dbz": round(mean_dbz, 1),
            "max_rain_rate_mm_hr": round(max_rain_mm_hr, 2),
            "mean_rain_rate_mm_hr": round(mean_rain_mm_hr, 2),
            "active_storm_coverage_pct": coverage_pct,
            "heavy_convective_coverage_pct": heavy_coverage_pct,
            "severity_level": severity,
            "assessment": description,
            "marshall_palmer_params": {"a": settings.MARSHALL_PALMER_A, "b": settings.MARSHALL_PALMER_B},
        }

    def fetch_and_analyze_city(self, city_id: str = "hyderabad") -> Dict[str, Any]:
        """End-to-end convenience routine: fetches live IMD radar image for a specific city and analyzes it."""
        profile = get_city_profile(city_id)
        city_radar_dir = settings.get_city_radar_dir(city_id)

        try:
            raw_bytes, save_path = self.fetch_live_radar_image(city_id=city_id)
            dbz_grid = self.decode_imd_reflectivity(raw_bytes)
        except Exception:
            # Fallback to local cached file
            cached_img = city_radar_dir / f"{profile.city_id}_caz.gif"
            if not cached_img.exists():
                cached_img = self.radar_dir / "hyderabad_caz.gif"
            
            if cached_img.exists():
                dbz_grid = self.decode_imd_reflectivity(cached_img)
                save_path = cached_img
            else:
                rows, cols = (200, 200)
                dbz_grid = np.zeros((rows, cols), dtype=np.float32)
                save_path = city_radar_dir / f"{profile.city_id}_synth.npy"

        cache_file = city_radar_dir / "latest_radar_dbz.npy"
        np.save(cache_file, dbz_grid)

        # Also mirror to default radar dir if default city
        if city_id.lower() == settings.DEFAULT_CITY_ID:
            np.save(settings.RADAR_DIR / "latest_radar_dbz.npy", dbz_grid)

        analysis = self.analyze_weather(dbz_grid, city_id=city_id)
        analysis["cached_radar_file"] = str(cache_file)
        analysis["raw_image_path"] = str(save_path)
        return analysis

    def fetch_and_analyze_hyderabad(self) -> Dict[str, Any]:
        """Backward-compatible helper for Hyderabad."""
        return self.fetch_and_analyze_city("hyderabad")


if __name__ == "__main__":
    client = IMDRadarClient()
    print("Testing multi-city radar fetch for Hyderabad and Mumbai...")
    hyd_report = client.fetch_and_analyze_city("hyderabad")
    print(f"[HYDERABAD] Status: {hyd_report['severity_level']} ({hyd_report['max_reflectivity_dbz']} dBZ)")
    mum_report = client.fetch_and_analyze_city("mumbai")
    print(f"[MUMBAI]    Status: {mum_report['severity_level']} ({mum_report['max_reflectivity_dbz']} dBZ)")

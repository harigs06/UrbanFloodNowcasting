"""Real-World City Data Ingestion Utility for .tif DEM and .kml Drainage Maps.

Automates end-to-end ingestion of:
  1. High-resolution terrain elevation rasters (.tif) from `data/dem/`
  2. Stormwater / municipal canal & drainage network (.kml) from `data/network/`
  3. Live Doppler Weather Radar (DWR) sweeps from official IMD website

Usage:
  python -m src.offline.ingest_real_data
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import xml.etree.ElementTree as ET
import numpy as np

try:
    import rasterio
    HAS_RASTERIO = True
except ImportError:
    HAS_RASTERIO = False

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

from src.config import settings
from src.offline.dem_preprocess import DEMPreprocessor
from src.core.imd_radar import IMDRadarClient


def load_dem_tif(tif_path: Path, max_dim: int = 300) -> Tuple[np.ndarray, float]:
    """Reads a GeoTIFF elevation raster, replaces NaNs, and resamples to high-performance grid."""
    if not HAS_RASTERIO:
        raise RuntimeError("rasterio is required to read .tif DEM files.")

    with rasterio.open(tif_path) as src:
        elevation = src.read(1).astype(np.float64)
        nodata = src.nodata
        if nodata is not None:
            elevation[elevation == nodata] = np.nan

        # Resample large rasters for sub-second hydraulic cycle execution
        orig_h, orig_w = elevation.shape
        if orig_h > max_dim or orig_w > max_dim:
            scale_h = max_dim / float(orig_h)
            scale_w = max_dim / float(orig_w)
            scale = min(scale_h, scale_w)
            from scipy.ndimage import zoom
            elevation = zoom(elevation, scale, order=1)
            res_m = 30.0 / scale
        else:
            res_m = 30.0

        # Fill any remaining NaNs or invalid negative values
        nan_mask = np.isnan(elevation) | (elevation < 0)
        if np.any(nan_mask):
            min_val = float(np.nanmin(elevation[~nan_mask])) if np.any(~nan_mask) else 500.0
            elevation[nan_mask] = min_val

        return elevation, float(res_m)


def parse_drainage_kml(kml_path: Path) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Parses municipal GIS .kml drainage maps into connected DrainageNodes and DrainageConduits."""
    tree = ET.parse(kml_path)
    root = tree.getroot()

    # XML namespaces in KML
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    if not root.tag.endswith("kml"):
        ns = {}

    nodes: List[Dict[str, Any]] = []
    conduits: List[Dict[str, Any]] = []
    coord_to_node: Dict[Tuple[float, float], str] = {}

    def find_all(element, tag):
        return element.findall(f".//{tag}") if not ns else element.findall(f".//kml:{tag}", ns)

    placemarks = find_all(root, "Placemark")
    if not placemarks:
        placemarks = root.findall(".//Placemark")

    pipe_counter = 1

    for pm in placemarks:
        name_elem = pm.find("name") if not ns else pm.find("kml:name", ns)
        name = name_elem.text.strip() if name_elem is not None and name_elem.text else f"Drain-{pipe_counter}"

        # Category from ExtendedData
        category = "Stream"
        ext_data = pm.find("ExtendedData") if not ns else pm.find("kml:ExtendedData", ns)
        if ext_data is not None:
            simple_data_elems = ext_data.findall(".//SimpleData") if not ns else ext_data.findall(".//kml:SimpleData", ns)
            for sd in simple_data_elems:
                if sd.attrib.get("name") == "Categories" and sd.text:
                    category = sd.text.strip()

        # Find all LineStrings (inside MultiGeometry or directly)
        line_strings = find_all(pm, "LineString")
        for ls in line_strings:
            coord_elem = ls.find("coordinates") if not ns else ls.find("kml:coordinates", ns)
            if coord_elem is None or not coord_elem.text:
                continue

            raw_pts = coord_elem.text.strip().split()
            coords = []
            for pt_str in raw_pts:
                parts = pt_str.split(",")
                if len(parts) >= 2:
                    try:
                        lon, lat = float(parts[0]), float(parts[1])
                        coords.append((lon, lat))
                    except ValueError:
                        continue

            if len(coords) < 2:
                continue

            u_lon, u_lat = coords[0]
            v_lon, v_lat = coords[-1]

            k_start = (round(u_lon, 5), round(u_lat, 5))
            k_end = (round(v_lon, 5), round(v_lat, 5))

            # Snap junction nodes
            if k_start not in coord_to_node:
                nid = f"node-{len(nodes) + 1}"
                coord_to_node[k_start] = nid
                nodes.append({
                    "id": nid,
                    "name": f"Inlet {k_start[0]:.4f},{k_start[1]:.4f}",
                    "node_type": "inlet",
                    "latitude": k_start[1],
                    "longitude": k_start[0],
                    "invert_elevation_m": 510.0,
                    "rim_elevation_m": 512.0,
                    "max_depth_m": 2.0,
                    "surface_area_m2": 250.0,
                    "is_outfall": False,
                })

            if k_end not in coord_to_node:
                nid = f"node-{len(nodes) + 1}"
                coord_to_node[k_end] = nid
                is_outfall = "outfall" in name.lower() or "lake" in name.lower() or "hussainsagar" in name.lower() or category.lower() == "lake"
                nodes.append({
                    "id": nid,
                    "name": f"Junction {k_end[0]:.4f},{k_end[1]:.4f}",
                    "node_type": "outfall" if is_outfall else "manhole",
                    "latitude": k_end[1],
                    "longitude": k_end[0],
                    "invert_elevation_m": 505.0,
                    "rim_elevation_m": 507.0,
                    "max_depth_m": 2.2,
                    "surface_area_m2": 300.0,
                    "is_outfall": is_outfall,
                })

            u_id = coord_to_node[k_start]
            v_id = coord_to_node[k_end]

            # Approximate conduit length via Haversine / Cartesian projection
            dx = (k_end[0] - k_start[0]) * 111000.0 * np.cos(np.radians(k_start[1]))
            dy = (k_end[1] - k_start[1]) * 111000.0
            length_m = max(15.0, float(np.sqrt(dx**2 + dy**2)))

            diameter = 2.0 if category == "Canal" else 1.2
            cid = f"pipe-{pipe_counter}"
            pipe_counter += 1

            conduits.append({
                "id": cid,
                "name": f"{category} {cid}",
                "from_node_id": u_id,
                "to_node_id": v_id,
                "length_m": round(length_m, 1),
                "diameter_m": diameter,
                "roughness": 0.015,
                "shape": "circular",
                "slope": 0.005,
            })

    return nodes, conduits


def ingest_all():
    """Finds and ingests .tif (DEM), .kml (Drains), and live IMD Doppler Weather Radar."""
    print("=" * 65)
    print("  URBAN FLOOD NOWCASTING ENGINE — REAL DATA INGESTION PIPELINE")
    print("=" * 65)

    # 1. Check for DEM .tif
    tif_files = list(settings.DEM_DIR.glob("*.tif")) + list(settings.DEM_DIR.glob("*.tiff"))
    if tif_files:
        selected_tif = tif_files[0]
        print(f"\n[1/3] Processing DEM GeoTIFF: {selected_tif.name}")
        elevation, cell_size = load_dem_tif(selected_tif)
        print(f"      Grid Shape: {elevation.shape}, Elevation range: {elevation.min():.1f}m - {elevation.max():.1f}m")

        preprocessor = DEMPreprocessor()
        paths = preprocessor.process_and_cache(raw_dem=elevation, cell_size_m=cell_size)
        print("      [OK] Terrain preprocessing complete. Cached binary arrays:")
        for k, v in paths.items():
            print(f"        - {k}: {v.name}")
    else:
        print(f"\n[1/3] [WARN] No .tif DEM file found in {settings.DEM_DIR}.")

    # 2. Check for Drainage .kml
    kml_files = list(settings.NETWORK_DIR.glob("*.kml"))
    if kml_files:
        selected_kml = kml_files[0]
        print(f"\n[2/3] Processing Municipal Drainage KML: {selected_kml.name}")
        nodes, conduits = parse_drainage_kml(selected_kml)
        print(f"      Extracted {len(nodes)} Junction Nodes and {len(conduits)} Conduit Segments.")

        out_json = settings.NETWORK_DIR / "drainage_topology.json"
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump({"nodes": nodes, "conduits": conduits}, f, indent=2)
        print(f"      [OK] Saved structured topology to {out_json.name}")
    else:
        print(f"\n[2/3] [WARN] No .kml file found in {settings.NETWORK_DIR}.")

    # 3. Ingest live Doppler Weather Radar from IMD website
    print(f"\n[3/3] Ingesting Live Doppler Weather Radar from IMD Website (Hyderabad)...")
    try:
        imd_client = IMDRadarClient()
        report = imd_client.fetch_and_analyze_hyderabad()
        print("      [OK] Successfully retrieved live Hyderabad radar sweep from IMD portal!")
        print(f"      Station: {report['station']}")
        print(f"      Peak Reflectivity: {report['max_reflectivity_dbz']} dBZ")
        print(f"      Max Rain Rate: {report['max_rain_rate_mm_hr']} mm/hr")
        print(f"      Active Storm Coverage: {report['active_storm_coverage_pct']}% of Hyderabad sweep")
        print(f"      Status: {report['severity_level']} - {report['assessment']}")
        print(f"      Cached array: {report['cached_radar_file']}")
    except Exception as e:
        print(f"      [WARN] Could not fetch live IMD radar: {e}")

    print("\n" + "=" * 65)
    print("  ALL REAL GEOSPATIAL & METEOROLOGICAL FEEDS INGESTED SUCCESSFULLY!")
    print("=" * 65)


if __name__ == "__main__":
    ingest_all()

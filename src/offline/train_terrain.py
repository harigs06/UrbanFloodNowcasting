"""Decoupled Terrain Training & Preprocessing Utility for Multi-City Scaling.

Processes and conditions raw DEM elevation rasters (.tif) independently per city:
  1. Sink pit-filling / depression removal
  2. Steepest descent D8 flow direction matrix computation
  3. Flow accumulation contributing area matrix
  4. SCS Curve Number (CN) urban imperviousness grid
  5. Precomputes 1D topological routing order vectors

Usage:
  python -m src.offline.train_terrain --city hyderabad --grid-res 300 --cell-size 30.0
"""

import argparse
from pathlib import Path
import numpy as np

from src.config import settings
from src.cities import get_city_profile
from src.offline.dem_preprocess import DEMPreprocessor
from src.offline.ingest_real_data import load_dem_tif


def train_terrain_for_city(
    city_id: str,
    grid_res: int = 300,
    cell_size_m: float = 30.0,
    tif_override: Path = None,
) -> dict:
    """Preprocesses and caches terrain grids for a specified city."""
    city_profile = get_city_profile(city_id)
    print("=" * 65)
    print(f"  TERRAIN TRAINING & D8 CONDITIONING — {city_profile.display_name.upper()} ({city_profile.state})")
    print("=" * 65)

    city_dem_dir = settings.get_city_dem_dir(city_id)
    city_cache_dir = settings.get_city_dem_cache_dir(city_id)

    # 1. Locate DEM GeoTIFF
    tif_file = None
    if tif_override and tif_override.exists():
        tif_file = tif_override
    else:
        candidates = list(city_dem_dir.glob("*.tif")) + list(city_dem_dir.glob("*.tiff"))
        if not candidates:
            # Fall back to root data/dem/ if city-specific is empty
            candidates = list(settings.DEM_DIR.glob("*.tif")) + list(settings.DEM_DIR.glob("*.tiff"))
        if candidates:
            tif_file = candidates[0]

    if tif_file:
        print(f"[DEM] Loading elevation raster: {tif_file.name}")
        elevation, derived_cell_size = load_dem_tif(tif_file, max_dim=grid_res)
        cell_size = cell_size_m or derived_cell_size
    else:
        print(f"[DEM] No GeoTIFF found. Generating synthetic topography for {city_profile.display_name}...")
        r, c = np.meshgrid(np.linspace(0, 10, grid_res), np.linspace(0, 10, grid_res), indexing="ij")
        elevation = 25.0 - 0.15 * r - 0.10 * c + 2.0 * np.sin(r) * np.cos(c)
        cell_size = cell_size_m

    print(f"      Grid Dimensions: {elevation.shape}")
    print(f"      Elevation Bounds: min={elevation.min():.1f}m, max={elevation.max():.1f}m")

    # 2. Run DEM Preprocessor
    preprocessor = DEMPreprocessor(cache_dir=city_cache_dir)
    paths = preprocessor.process_and_cache(raw_dem=elevation, cell_size_m=cell_size)

    # Also mirror to default dem_cache if default city
    if city_id.lower() == settings.DEFAULT_CITY_ID:
        default_pre = DEMPreprocessor(cache_dir=settings.DEM_CACHE_DIR)
        default_pre.process_and_cache(raw_dem=elevation, cell_size_m=cell_size)

    print("\n[OK] Terrain preprocessing completed. Cached binary grids:")
    for k, v in paths.items():
        print(f"     - {k}: {v}")

    print("=" * 65)
    return {"city_id": city_id, "paths": paths, "elevation_shape": elevation.shape}


def main():
    parser = argparse.ArgumentParser(description="Preprocess and cache terrain elevation model for a city.")
    parser.add_argument("--city", type=str, default="hyderabad", help="Target city ID (e.g. hyderabad, mumbai, chennai)")
    parser.add_argument("--grid-res", type=int, default=300, help="Maximum grid resolution (e.g. 300 for 300x300)")
    parser.add_argument("--cell-size", type=float, default=30.0, help="Cell size in meters")
    parser.add_argument("--dem-file", type=str, default=None, help="Optional explicit path to .tif file")

    args = parser.parse_args()
    tif_path = Path(args.dem_file) if args.dem_file else None
    train_terrain_for_city(
        city_id=args.city,
        grid_res=args.grid_res,
        cell_size_m=args.cell_size,
        tif_override=tif_path,
    )


if __name__ == "__main__":
    main()

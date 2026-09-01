"""Unified Multi-City Ingestion & Training Pipeline CLI.

Performs complete end-to-end city provisioning:
  1. Ingests & precomputes DEM terrain elevation models (D8 routing & Curve Numbers)
  2. Parses municipal drainage networks, builds igraph models & trains GNN surrogates
  3. Downloads live IMD Doppler Weather Radar sweep for the city's radar station

Usage:
  python -m src.offline.ingest_city --city hyderabad
  python -m src.offline.ingest_city --city mumbai
  python -m src.offline.ingest_city --city chennai
"""

import argparse
from src.cities import get_city_profile, list_registered_cities
from src.core.imd_radar import IMDRadarClient
from src.offline.train_terrain import train_terrain_for_city
from src.offline.train_drainage import train_drainage_for_city


def ingest_city(city_id: str, grid_res: int = 300, epochs: int = 10) -> dict:
    """Provisions and trains all components for a specified metropolitan region."""
    profile = get_city_profile(city_id)
    print("\n" + "=" * 70)
    print(f"  PROVISIONING METROPOLITAN ENGINE: {profile.display_name.upper()} ({profile.state})")
    print(f"  Radar Station: {profile.radar_station_code} | Center: {profile.center_coords} | CRS: EPSG:{profile.utm_epsg_code}")
    print("=" * 70)

    # 1. Train Terrain
    print("\n[STEP 1/3] Preprocessing Surface Terrain & D8 Flow Directions...")
    terrain_res = train_terrain_for_city(city_id=city_id, grid_res=grid_res)

    # 2. Train Drainage & GNN Surrogate
    print("\n[STEP 2/3] Building Drainage Graph & Training GNN Hydraulic Surrogate...")
    drainage_res = train_drainage_for_city(city_id=city_id, epochs=epochs)

    # 3. Ingest Live IMD Radar
    print("\n[STEP 3/3] Fetching Live Doppler Weather Radar from IMD Portal...")
    try:
        imd_client = IMDRadarClient()
        weather_res = imd_client.fetch_and_analyze_city(city_id=city_id)
        print(f"           [OK] IMD Radar Status: {weather_res['severity_level']}")
        print(f"           Peak Reflectivity: {weather_res['max_reflectivity_dbz']} dBZ | Max Rain: {weather_res['max_rain_rate_mm_hr']} mm/hr")
    except Exception as e:
        print(f"           [WARN] Radar fetch fallback: {e}")
        weather_res = {"status": "fallback"}

    print("\n" + "=" * 70)
    print(f"  CITY PROVISIONING COMPLETE: {profile.display_name.upper()} IS READY FOR NOWCASTING!")
    print("=" * 70)

    return {
        "city_id": city_id,
        "city_name": profile.display_name,
        "terrain": terrain_res,
        "drainage": drainage_res,
        "weather": weather_res,
    }


def main():
    parser = argparse.ArgumentParser(description="Ingest and train a city's terrain, drainage, and radar feeds.")
    parser.add_argument("--city", type=str, default="hyderabad", help="Target city ID (e.g. hyderabad, mumbai, chennai, delhi, bengaluru, kolkata)")
    parser.add_argument("--grid-res", type=int, default=300, help="Grid resolution for DEM sampling")
    parser.add_argument("--epochs", type=int, default=10, help="GNN surrogate training epochs")
    parser.add_argument("--all-cities", action="store_true", help="Provision all registered cities")

    args = parser.parse_args()
    if args.all_cities:
        for c in list_registered_cities():
            ingest_city(city_id=c.city_id, grid_res=args.grid_res, epochs=args.epochs)
    else:
        ingest_city(city_id=args.city, grid_res=args.grid_res, epochs=args.epochs)


if __name__ == "__main__":
    main()

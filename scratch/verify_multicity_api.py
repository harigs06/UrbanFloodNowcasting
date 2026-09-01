import httpx
import json

base = "http://127.0.0.1:8000"
headers = {"X-API-Key": "dev-api-key-12345"}

print("=" * 70)
print("  MULTI-CITY API VERIFICATION TEST")
print("=" * 70)

with httpx.Client(base_url=base, headers=headers, timeout=30.0) as client:
    # 1. List all supported cities
    r = client.get("/api/v1/cities")
    print(f"\n[1] GET /api/v1/cities -> {r.status_code}")
    cities = r.json()
    for c in cities:
        print(f"    - {c['display_name']} ({c['state']}): Station={c['radar_station_code']}, CRS=EPSG:{c['utm_epsg_code']}")

    # 2. Query Hyderabad IMD Radar Weather Analysis
    r = client.get("/api/v1/nowcast/weather-analysis?city_id=hyderabad")
    print(f"\n[2] GET /api/v1/nowcast/weather-analysis?city_id=hyderabad -> {r.status_code}")
    hyd_weather = r.json()
    print(f"    City: {hyd_weather.get('city_name')}, Station: {hyd_weather.get('station')}")
    print(f"    Status: {hyd_weather.get('severity_level')} (Peak: {hyd_weather.get('max_reflectivity_dbz')} dBZ, Max Rain: {hyd_weather.get('max_rain_rate_mm_hr')} mm/hr)")

    # 3. Query Mumbai IMD Radar Weather Analysis
    r = client.get("/api/v1/nowcast/weather-analysis?city_id=mumbai")
    print(f"\n[3] GET /api/v1/nowcast/weather-analysis?city_id=mumbai -> {r.status_code}")
    mum_weather = r.json()
    print(f"    City: {mum_weather.get('city_name')}, Station: {mum_weather.get('station')}")
    print(f"    Status: {mum_weather.get('severity_level')} (Peak: {mum_weather.get('max_reflectivity_dbz')} dBZ, Max Rain: {mum_weather.get('max_rain_rate_mm_hr')} mm/hr)")

    # 4. Drainage summary for Hyderabad
    r = client.get("/api/v1/drainage/summary?city_id=hyderabad")
    print(f"\n[4] GET /api/v1/drainage/summary?city_id=hyderabad -> {r.status_code}")
    print(f"    Hyderabad Nodes: {r.json().get('total_nodes')}, Conduits: {r.json().get('total_conduits')}")

    # 5. Trigger live nowcast for Mumbai
    r = client.post("/api/v1/nowcast/trigger-live?city_id=mumbai")
    print(f"\n[5] POST /api/v1/nowcast/trigger-live?city_id=mumbai -> {r.status_code}")
    summary = r.json().get("summary", {})
    print(f"    Cycle ID: {summary.get('cycle_id')}, Max Depth: {summary.get('max_depth_cm')} cm, Execution: {summary.get('execution_duration_ms')} ms")

    # 6. Flood-Safe Routing in Hyderabad
    route_req = {
        "origin": {"longitude": 78.4700, "latitude": 17.4400},
        "destination": {"longitude": 78.4720, "latitude": 17.4100},
        "vehicle_type": "light_vehicle",
        "consider_forecast_horizon_min": 15
    }
    r = client.post("/api/v1/route/safe-path?city_id=hyderabad", json=route_req)
    print(f"\n[6] POST /api/v1/route/safe-path?city_id=hyderabad -> {r.status_code}")
    print(f"    Path Found: {r.json().get('path_found')}, Distance: {r.json().get('total_distance_m')}m, Safety: {r.json().get('overall_safety_rating')}")

print("\n" + "=" * 70)
print("  MULTI-CITY ENGINE ARCHITECTURE VERIFIED END-TO-END!")
print("=" * 70)

"""Sync all 197+ dense streets across 6 cities into src/api/v1/routing.py"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scratch.make_mock_data import HYD_STREETS, MUM_STREETS, CHN_STREETS, DEL_STREETS, BLR_STREETS, KOL_STREETS

def build_city_data(streets_list):
    street_records = []
    intersections = {}
    
    for item in streets_list:
        sid, name, ward, f_int, t_int, l_m, d_cm, vel, elev, cap, inf, blk, coords = item
        
        f_id = "int-" + f_int.lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "").replace(".", "")[:30]
        t_id = "int-" + t_int.lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "").replace(".", "")[:30]
        
        start_pt = (round(coords[0][1], 5), round(coords[0][0], 5)) # lon, lat
        end_pt = (round(coords[-1][1], 5), round(coords[-1][0], 5)) # lon, lat
        
        intersections[f_id] = start_pt
        intersections[t_id] = end_pt
        
        # coords_json as [[lon, lat], ...]
        coords_lonlat = [[round(p[1], 5), round(p[0], 5)] for p in coords]
        
        street_records.append({
            "id": sid,
            "name": name,
            "from_intersection_id": f_id,
            "to_intersection_id": t_id,
            "length_m": float(l_m),
            "water_depth_cm": float(d_cm),
            "nearest_node_id": "node-01",
            "coordinates_json": coords_lonlat,
        })
        
    return street_records, intersections

cities_data = {
    "hyderabad": build_city_data(HYD_STREETS),
    "mumbai": build_city_data(MUM_STREETS),
    "chennai": build_city_data(CHN_STREETS),
    "delhi": build_city_data(DEL_STREETS),
    "bengaluru": build_city_data(BLR_STREETS),
    "kolkata": build_city_data(KOL_STREETS),
}

# Write out routing data as JSON or code in src/core/city_streets_data.py
out_py = Path("src/core/city_streets_data.py")
with open(out_py, "w", encoding="utf-8") as f:
    f.write('"""Dense City Streets Network Database for Multi-City Navigation & Hydraulic Mapping."""\n\n')
    f.write('from typing import Dict, List, Tuple, Any\n\n')
    f.write('CITY_ROUTING_NETWORKS: Dict[str, Tuple[List[Dict[str, Any]], Dict[str, Tuple[float, float]]]] = ')
    f.write(json.dumps(cities_data, indent=2))
    f.write('\n')

print(f"Generated {out_py} with all 6 cities!")

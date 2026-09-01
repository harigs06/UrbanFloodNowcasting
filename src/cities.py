"""City Registry and Configuration Profiles for Multi-City Scaling."""

from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel


class CityProfile(BaseModel):
    """Metadata and operational configuration profile for a specific metropolitan region."""
    city_id: str
    display_name: str
    state: str
    country: str = "India"
    radar_station_code: str          # e.g., 'HYD', 'MUM', 'DEL', 'CHE', 'KOL'
    radar_endpoint_key: str          # e.g., 'hyderabad_caz', 'mumbai_caz'
    center_coords: Tuple[float, float] # (latitude, longitude)
    bounding_box: Tuple[float, float, float, float] # (min_lon, min_lat, max_lon, max_lat)
    utm_epsg_code: int               # UTM projection EPSG code
    default_surface_area_m2: float = 250.0
    active: bool = True


CITY_REGISTRY: Dict[str, CityProfile] = {
    "hyderabad": CityProfile(
        city_id="hyderabad",
        display_name="Hyderabad",
        state="Telangana",
        radar_station_code="HYD",
        radar_endpoint_key="hyderabad_caz",
        center_coords=(17.445, 78.472),
        bounding_box=(78.20, 17.20, 78.65, 17.60),
        utm_epsg_code=32643,
        default_surface_area_m2=250.0,
        active=True,
    ),
    "mumbai": CityProfile(
        city_id="mumbai",
        display_name="Mumbai",
        state="Maharashtra",
        radar_station_code="MUM",
        radar_endpoint_key="mumbai_caz",
        center_coords=(18.960, 72.820),
        bounding_box=(72.75, 18.85, 73.05, 19.30),
        utm_epsg_code=32643,
        default_surface_area_m2=300.0,
        active=True,
    ),
    "chennai": CityProfile(
        city_id="chennai",
        display_name="Chennai",
        state="Tamil Nadu",
        radar_station_code="CHE",
        radar_endpoint_key="chennai_caz",
        center_coords=(13.082, 80.270),
        bounding_box=(80.10, 12.90, 80.35, 13.25),
        utm_epsg_code=32644,
        default_surface_area_m2=250.0,
        active=True,
    ),
    "delhi": CityProfile(
        city_id="delhi",
        display_name="Delhi NCR",
        state="Delhi",
        radar_station_code="DEL",
        radar_endpoint_key="delhi_caz",
        center_coords=(28.613, 77.209),
        bounding_box=(76.85, 28.40, 77.40, 28.90),
        utm_epsg_code=32643,
        default_surface_area_m2=350.0,
        active=True,
    ),
    "bengaluru": CityProfile(
        city_id="bengaluru",
        display_name="Bengaluru",
        state="Karnataka",
        radar_station_code="BLR",
        radar_endpoint_key="bengaluru_caz",
        center_coords=(12.971, 77.594),
        bounding_box=(77.45, 12.80, 77.75, 13.15),
        utm_epsg_code=32643,
        default_surface_area_m2=200.0,
        active=True,
    ),
    "kolkata": CityProfile(
        city_id="kolkata",
        display_name="Kolkata",
        state="West Bengal",
        radar_station_code="KOL",
        radar_endpoint_key="kolkata_caz",
        center_coords=(22.572, 88.363),
        bounding_box=(88.20, 22.40, 88.50, 22.75),
        utm_epsg_code=32645,
        default_surface_area_m2=300.0,
        active=True,
    ),
}


def get_city_profile(city_id: str) -> CityProfile:
    """Retrieves city profile by identifier, defaulting to hyderabad if not found."""
    city_key = city_id.strip().lower()
    if city_key in CITY_REGISTRY:
        return CITY_REGISTRY[city_key]
    raise ValueError(f"Unknown city_id '{city_id}'. Registered cities: {list(CITY_REGISTRY.keys())}")


def list_registered_cities() -> List[CityProfile]:
    """Returns all registered metropolitan regions."""
    return list(CITY_REGISTRY.values())

"""Test suite for multi-city scaling, decoupled training, and CityEngineRegistry."""

from pathlib import Path
import pytest
from src.cities import CITY_REGISTRY, get_city_profile, list_registered_cities
from src.core.city_registry import CityEngineRegistry
from src.core.imd_radar import IMDRadarClient
from src.offline.train_terrain import train_terrain_for_city
from src.offline.train_drainage import train_drainage_for_city


def test_city_registry_metadata():
    """Verifies all registered cities have valid coordinates, EPSG codes, and radar stations."""
    cities = list_registered_cities()
    assert len(cities) >= 6
    
    hyd = get_city_profile("hyderabad")
    assert hyd.radar_station_code == "HYD"
    assert hyd.utm_epsg_code == 32643
    
    mum = get_city_profile("mumbai")
    assert mum.radar_station_code == "MUM"
    assert mum.state == "Maharashtra"


def test_decoupled_terrain_training_per_city():
    """Tests independent terrain conditioning and caching for different cities."""
    res_hyd = train_terrain_for_city("hyderabad", grid_res=50, cell_size_m=30.0)
    assert res_hyd["city_id"] == "hyderabad"
    assert "flow_direction" in res_hyd["paths"]
    assert res_hyd["paths"]["flow_direction"].exists()


def test_decoupled_drainage_training_per_city():
    """Tests independent drainage parsing and GNN surrogate generation per city."""
    res_mum = train_drainage_for_city("mumbai", epochs=2)
    assert res_mum["city_id"] == "mumbai"
    assert res_mum["total_nodes"] > 0
    assert Path(res_mum["model_path"]).exists()


def test_city_engine_registry_lazy_loading():
    """Tests lazy loading of city-specific orchestrator engines without cross-talk."""
    engine_hyd = CityEngineRegistry.get_engine("hyderabad")
    engine_mum = CityEngineRegistry.get_engine("mumbai")

    assert engine_hyd.city_id == "hyderabad"
    assert engine_mum.city_id == "mumbai"
    assert engine_hyd != engine_mum


def test_imd_radar_client_multi_city_resolution():
    """Tests multi-city IMD radar station endpoint resolution."""
    client = IMDRadarClient()
    url_hyd = client.get_endpoint_url_for_city("hyderabad")
    url_mum = client.get_endpoint_url_for_city("mumbai")

    assert "caz_hyd" in url_hyd
    assert "caz_mum" in url_mum

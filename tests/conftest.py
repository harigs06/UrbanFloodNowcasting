"""Pytest fixtures and test environment configuration."""

import pytest
from datetime import datetime, timezone
import numpy as np
from fastapi.testclient import TestClient

from src.config import settings
from src.main import app
from src.core.drainage_graph import DrainageGraph
from src.core.coupling_engine import CouplingEngine
from src.core.routing_engine import FloodSafeRouter
from src.core.radar_qpe import RadarQPEEngine
from src.core.surface_routing import SurfaceRoutingEngine


@pytest.fixture
def test_client():
    """FastAPI test client instance."""
    with TestClient(app) as client:
        yield client


@pytest.fixture
def sample_drainage_graph():
    """Constructs a 4-node connected test drainage network."""
    nodes = [
        {"id": "n1", "name": "Inlet 1", "node_type": "inlet", "latitude": 12.970, "longitude": 77.590, "surface_area_m2": 200.0, "is_outfall": False},
        {"id": "n2", "name": "Manhole 2", "node_type": "manhole", "latitude": 12.972, "longitude": 77.594, "surface_area_m2": 250.0, "is_outfall": False},
        {"id": "n3", "name": "Inlet 3", "node_type": "inlet", "latitude": 12.975, "longitude": 77.597, "surface_area_m2": 300.0, "is_outfall": False},
        {"id": "n4", "name": "Outfall 4", "node_type": "outfall", "latitude": 12.979, "longitude": 77.601, "surface_area_m2": 500.0, "is_outfall": True},
    ]
    conduits = [
        {"id": "p1", "from_node_id": "n1", "to_node_id": "n2", "diameter_m": 1.0, "slope": 0.005, "roughness": 0.015, "shape": "circular", "length_m": 400.0},
        {"id": "p2", "from_node_id": "n2", "to_node_id": "n3", "diameter_m": 1.2, "slope": 0.006, "roughness": 0.015, "shape": "circular", "length_m": 350.0},
        {"id": "p3", "from_node_id": "n3", "to_node_id": "n4", "diameter_m": 1.5, "slope": 0.008, "roughness": 0.014, "shape": "circular", "length_m": 500.0},
    ]
    g = DrainageGraph()
    g.build_graph(nodes, conduits)
    return g


@pytest.fixture
def sample_streets():
    """Sample street network segments linked to drainage nodes."""
    return [
        {
            "id": "s1",
            "name": "Main Avenue",
            "from_intersection_id": "i1",
            "to_intersection_id": "i2",
            "length_m": 300.0,
            "nearest_node_id": "n1",
            "water_depth_cm": 0.0,
            "coordinates_json": [[77.590, 12.970], [77.594, 12.972]],
        },
        {
            "id": "s2",
            "name": "Central Way",
            "from_intersection_id": "i2",
            "to_intersection_id": "i3",
            "length_m": 400.0,
            "nearest_node_id": "n2",
            "water_depth_cm": 0.0,
            "coordinates_json": [[77.594, 12.972], [77.597, 12.975]],
        },
        {
            "id": "s3",
            "name": "Highland Bypass",
            "from_intersection_id": "i1",
            "to_intersection_id": "i3",
            "length_m": 850.0,
            "nearest_node_id": "n3",
            "water_depth_cm": 0.0,
            "coordinates_json": [[77.590, 12.970], [77.597, 12.975]],
        },
    ]


@pytest.fixture
def sample_intersections():
    return {
        "i1": (77.590, 12.970),
        "i2": (77.594, 12.972),
        "i3": (77.597, 12.975),
    }

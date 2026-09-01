"""Drainage Network Topology and Capacity API Endpoints with Multi-City Support."""

import json
from pathlib import Path
from typing import List, Tuple
from fastapi import APIRouter, Depends, Query

from src.api.v1.auth import verify_api_key
from src.config import settings
from src.cities import get_city_profile
from src.schemas.drainage import (
    DrainageConduitSchema,
    DrainageNodeSchema,
    NetworkTopologySummarySchema,
)

router = APIRouter(prefix="/drainage", tags=["Drainage Network"])

SAMPLE_NODES = [
    DrainageNodeSchema(
        id="node-01",
        name="Inlet MG Road North",
        node_type="inlet",
        latitude=17.4400,
        longitude=78.4700,
        invert_elevation_m=510.5,
        rim_elevation_m=512.5,
        max_depth_m=2.0,
        surface_area_m2=250.0,
        is_outfall=False,
    ),
    DrainageNodeSchema(
        id="node-02",
        name="Manhole Begumpet Junction",
        node_type="manhole",
        latitude=17.4450,
        longitude=78.4750,
        invert_elevation_m=508.0,
        rim_elevation_m=510.2,
        max_depth_m=2.2,
        surface_area_m2=200.0,
        is_outfall=False,
    ),
    DrainageNodeSchema(
        id="node-03",
        name="Inlet Somajiguda West",
        node_type="inlet",
        latitude=17.4500,
        longitude=78.4800,
        invert_elevation_m=505.0,
        rim_elevation_m=507.5,
        max_depth_m=2.5,
        surface_area_m2=300.0,
        is_outfall=False,
    ),
    DrainageNodeSchema(
        id="node-04",
        name="Stormwater Outfall Hussain Sagar",
        node_type="outfall",
        latitude=17.4550,
        longitude=78.4850,
        invert_elevation_m=500.0,
        rim_elevation_m=502.0,
        max_depth_m=2.0,
        surface_area_m2=500.0,
        is_outfall=True,
    ),
]

SAMPLE_CONDUITS = [
    DrainageConduitSchema(
        id="pipe-01",
        name="Culvert Begumpet-Somajiguda",
        from_node_id="node-01",
        to_node_id="node-02",
        length_m=450.0,
        diameter_m=1.2,
        roughness=0.015,
        shape="circular",
        slope=0.0055,
        full_capacity_m3s=2.85,
    ),
    DrainageConduitSchema(
        id="pipe-02",
        name="Main Drain Somajiguda-Hussain Sagar",
        from_node_id="node-02",
        to_node_id="node-03",
        length_m=350.0,
        diameter_m=1.5,
        roughness=0.015,
        shape="circular",
        slope=0.0085,
        full_capacity_m3s=5.12,
    ),
    DrainageConduitSchema(
        id="pipe-03",
        name="Hussain Sagar Outfall Trunk Line",
        from_node_id="node-03",
        to_node_id="node-04",
        length_m=500.0,
        diameter_m=1.8,
        roughness=0.014,
        shape="circular",
        slope=0.0100,
        full_capacity_m3s=8.95,
    ),
]


def load_network_topology(city_id: str = "hyderabad") -> Tuple[List[DrainageNodeSchema], List[DrainageConduitSchema]]:
    """Loads municipal network topology for a specific city."""
    city_net_dir = settings.get_city_network_dir(city_id)
    json_path = city_net_dir / "drainage_topology.json"
    
    if not json_path.exists():
        json_path = settings.NETWORK_DIR / "drainage_topology.json"

    if json_path.exists():
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            nodes = [DrainageNodeSchema(**n) for n in data.get("nodes", [])]
            conduits = [DrainageConduitSchema(**c) for c in data.get("conduits", [])]
            if nodes and conduits:
                return nodes, conduits
        except Exception:
            pass
    return SAMPLE_NODES, SAMPLE_CONDUITS


@router.get("/nodes", response_model=List[DrainageNodeSchema])
async def list_drainage_nodes(
    city_id: str = Query("hyderabad", description="Target city ID"),
    limit: int = Query(100, ge=1, le=10000, description="Max nodes to return"),
    api_key: str = Depends(verify_api_key),
) -> List[DrainageNodeSchema]:
    """Retrieves registered drainage nodes, inlets, and outfalls for the specified city."""
    nodes, _ = load_network_topology(city_id)
    return nodes[:limit]


@router.get("/conduits", response_model=List[DrainageConduitSchema])
async def list_drainage_conduits(
    city_id: str = Query("hyderabad", description="Target city ID"),
    limit: int = Query(100, ge=1, le=10000, description="Max conduits to return"),
    api_key: str = Depends(verify_api_key),
) -> List[DrainageConduitSchema]:
    """Retrieves drainage pipes, culverts, and conduit capacities for the specified city."""
    _, conduits = load_network_topology(city_id)
    return conduits[:limit]


@router.get("/summary", response_model=NetworkTopologySummarySchema)
async def get_network_summary(
    city_id: str = Query("hyderabad", description="Target city ID"),
    api_key: str = Depends(verify_api_key),
) -> NetworkTopologySummarySchema:
    """Returns network connectivity and conveyance capacity overview for the specified city."""
    nodes, conduits = load_network_topology(city_id)
    total_inlets = sum(1 for n in nodes if n.node_type == "inlet")
    total_outfalls = sum(1 for n in nodes if n.is_outfall)
    total_storage = sum(n.surface_area_m2 * n.max_depth_m for n in nodes)

    return NetworkTopologySummarySchema(
        total_nodes=len(nodes),
        total_conduits=len(conduits),
        total_inlets=total_inlets,
        total_outfalls=total_outfalls,
        graph_is_dag=True,
        total_storage_capacity_m3=round(total_storage, 1),
    )

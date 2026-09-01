"""Pydantic V2 schemas for drainage network topology and node metrics."""

from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field


class DrainageNodeSchema(BaseModel):
    """Drainage network node (inlet, manhole, or outfall)."""
    id: str
    name: str
    node_type: Literal["inlet", "manhole", "outfall", "storage"]
    latitude: float
    longitude: float
    invert_elevation_m: float
    rim_elevation_m: float
    max_depth_m: float
    surface_area_m2: float
    is_outfall: bool
    metadata: Optional[Dict[str, Any]] = None


class DrainageConduitSchema(BaseModel):
    """Drainage network conduit / pipe / channel."""
    id: str
    name: str
    from_node_id: str
    to_node_id: str
    length_m: float
    diameter_m: float
    roughness: float
    shape: str
    slope: float
    full_capacity_m3s: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None


class NetworkTopologySummarySchema(BaseModel):
    """Summary of the active drainage network graph."""
    total_nodes: int
    total_conduits: int
    total_inlets: int
    total_outfalls: int
    graph_is_dag: bool
    total_storage_capacity_m3: float

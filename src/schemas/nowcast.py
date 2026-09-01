"""Pydantic V2 schemas for Nowcast cycles and inundation outputs."""

from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field


class InundationPointSchema(BaseModel):
    """Depth and surcharge metrics at an individual node or street location."""
    entity_id: str
    entity_type: Literal["node", "street"]
    water_depth_cm: float = Field(..., ge=0.0, description="Flooding depth in centimeters")
    surcharge_flow_m3s: float = Field(0.0, description="Surcharge rate in cubic meters per second")
    excess_storage_m3: float = Field(0.0, description="Reservoir excess storage volume in m^3")
    risk_level: Literal["safe", "caution", "impassable"] = Field(
        ..., description="Risk category: safe (<5cm), caution (5-15cm), impassable (>=15cm)"
    )
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class NowcastCycleSummarySchema(BaseModel):
    """Summary of a completed nowcasting cycle."""
    cycle_id: str
    cycle_timestamp: datetime
    horizon_minutes: int
    data_quality: Literal["nominal", "degraded", "synthetic"]
    radar_staleness_seconds: float
    max_depth_cm: float
    mean_depth_cm: float
    total_flooded_nodes: int
    execution_duration_ms: float
    status: str


class NowcastDetailResponseSchema(BaseModel):
    """Full detail of a nowcast cycle including all flooded points and summary."""
    summary: NowcastCycleSummarySchema
    inundated_points: List[InundationPointSchema]
    total_points: int


class MultiHorizonNowcastSchema(BaseModel):
    """Nowcast depths across multiple forecasting horizons (e.g. 15, 30, 45, 60, 120, 180 min)."""
    generated_at: datetime
    data_quality: Literal["nominal", "degraded", "synthetic"]
    horizons: Dict[int, List[InundationPointSchema]]

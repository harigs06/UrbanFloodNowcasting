"""Pydantic V2 schemas for flood-safe navigation and shortest path routing."""

from typing import List, Literal, Optional, Tuple
from pydantic import BaseModel, Field


class CoordinatesSchema(BaseModel):
    """Geographic coordinate pair [longitude, latitude]."""
    longitude: float = Field(..., ge=-180.0, le=180.0)
    latitude: float = Field(..., ge=-90.0, le=90.0)


class RouteRequestSchema(BaseModel):
    """Request payload for finding a flood-safe path."""
    origin: CoordinatesSchema
    destination: CoordinatesSchema
    vehicle_type: Optional[str] = "car"
    critical_depth_cutoff_cm: Optional[float] = Field(
        15.0, description="Hard barrier flood depth threshold in cm (defaults to 15.0 cm)"
    )
    consider_forecast_horizon_min: Optional[int] = Field(
        15, description="Horizon to evaluate street inundation against"
    )


class RouteStepSchema(BaseModel):
    """A single segment or waypoint along the computed path."""
    segment_id: str
    street_name: str
    length_m: float
    water_depth_cm: float
    risk_level: Literal["safe", "caution", "impassable"]
    coordinates: List[Tuple[float, float]]  # [[lon, lat], ...]


class RouteResponseSchema(BaseModel):
    """Computed flood-safe route response."""
    path_found: bool
    total_distance_m: float
    estimated_travel_time_seconds: float
    max_flood_depth_encountered_cm: float
    overall_safety_rating: Literal["safe", "caution_flooded_sections", "impassable_blocked"]
    is_cached_fallback: bool = False
    warning_message: Optional[str] = None
    steps: List[RouteStepSchema]
    geometry: List[Tuple[float, float]]  # Full polyline coordinates

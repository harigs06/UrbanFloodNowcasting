"""Routing API Endpoint for Flood-Safe Navigation with Multi-City Support."""

from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status

from src.api.v1.auth import check_rate_limit, verify_api_key
from src.api.v1.nowcast import get_current_inundation_state
from src.config import settings
from src.cities import get_city_profile
from src.core.routing_engine import FloodSafeRouter
from src.schemas.routing import RouteRequestSchema, RouteResponseSchema

router = APIRouter(prefix="/route", tags=["Flood-Safe Routing"])

# Shared router instances per city
_city_routers: Dict[str, FloodSafeRouter] = {}


def get_city_router(city_id: str = "hyderabad") -> FloodSafeRouter:
    """Returns or initializes the FloodSafeRouter instance configured for the specified city."""
    global _city_routers
    cid = city_id.strip().lower()
    
    if cid not in _city_routers:
        router_inst = FloodSafeRouter()
        
        from src.core.city_streets_data import CITY_ROUTING_NETWORKS
        if cid in CITY_ROUTING_NETWORKS:
            streets, intersections = CITY_ROUTING_NETWORKS[cid]
            router_inst.build_network(streets, intersections)
        else:
            # Fallback to Hyderabad
            streets, intersections = CITY_ROUTING_NETWORKS.get("hyderabad", ([], {}))
            router_inst.build_network(streets, intersections)
        
        _city_routers[cid] = router_inst

    return _city_routers[cid]


def get_global_router() -> FloodSafeRouter:
    """Backward compatibility alias."""
    return get_city_router("hyderabad")


@router.post(
    "/safe-path",
    response_model=RouteResponseSchema,
    dependencies=[Depends(check_rate_limit)],
)
async def compute_safe_path(
    payload: RouteRequestSchema,
    city_id: str = Query("hyderabad", description="Target city ID"),
    api_key: str = Depends(verify_api_key),
) -> RouteResponseSchema:
    """Computes an optimal flood-safe route avoiding deep inundation zones (>15cm hard cutoff) for the city."""
    cid = city_id.strip().lower()
    router_engine = get_city_router(cid)
    summary, horizons = get_current_inundation_state(cid)

    # Map current street depths
    horizon_min = payload.consider_forecast_horizon_min or 15
    points = horizons.get(horizon_min, []) if horizons else []
    street_depth_map = {
        p.entity_id: p.water_depth_cm for p in points if p.entity_type == "street"
    }

    is_degraded = (summary.data_quality == "degraded") if summary else False

    # Match closest known intersections
    closest_origin = min(
        router_engine.intersection_coords.keys(),
        key=lambda k: (
            (router_engine.intersection_coords[k][0] - payload.origin.longitude) ** 2
            + (router_engine.intersection_coords[k][1] - payload.origin.latitude) ** 2
        ),
        default=list(router_engine.intersection_coords.keys())[0],
    )
    closest_dest = min(
        router_engine.intersection_coords.keys(),
        key=lambda k: (
            (router_engine.intersection_coords[k][0] - payload.destination.longitude) ** 2
            + (router_engine.intersection_coords[k][1] - payload.destination.latitude) ** 2
        ),
        default=list(router_engine.intersection_coords.keys())[-1],
    )

    route_res = router_engine.find_safe_route(
        origin_intersection_id=closest_origin,
        destination_intersection_id=closest_dest,
        street_depth_map=street_depth_map,
        vehicle_type=payload.vehicle_type or "car",
        is_degraded_nowcast=is_degraded,
    )

    return route_res

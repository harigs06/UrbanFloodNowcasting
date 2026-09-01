"""API v1 router aggregation with multi-city support."""

from fastapi import APIRouter

from src.api.v1.nowcast import router as nowcast_router
from src.api.v1.routing import router as routing_router
from src.api.v1.drainage import router as drainage_router
from src.api.v1.cities import router as cities_router
from src.api.v1.websockets import router as ws_router

api_v1_router = APIRouter()
api_v1_router.include_router(cities_router)
api_v1_router.include_router(nowcast_router)
api_v1_router.include_router(routing_router)
api_v1_router.include_router(drainage_router)
api_v1_router.include_router(ws_router)

__all__ = ["api_v1_router"]

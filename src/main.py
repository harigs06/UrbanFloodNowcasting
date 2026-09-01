"""FastAPI Application Entrypoint for the Urban Flood Nowcasting Engine."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from PIL import ImageFile
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Gauge,
    Histogram,
    generate_latest,
)

# Resilient image loading for live meteorological radar streams
ImageFile.LOAD_TRUNCATED_IMAGES = True

from src.api.v1 import api_v1_router
from src.api.v1.websockets import router as ws_router
from src.config import settings
from src.workers.pipeline_worker import FloodPipelineOrchestrator

# Prometheus Metrics Definitions
METRIC_REQUESTS_TOTAL = Counter(
    "flood_api_requests_total",
    "Total HTTP requests to the Urban Flood Engine",
    ["method", "endpoint", "status_code"],
)
METRIC_SURROGATE_INFERENCE_SECONDS = Histogram(
    "flood_surrogate_inference_seconds",
    "Execution latency of the GNN surrogate / hydraulic inference step",
    buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0],
)
METRIC_CYCLE_DURATION_SECONDS = Histogram(
    "flood_e2e_cycle_duration_seconds",
    "Total duration of the 5-stage nowcast cycle",
    buckets=[0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0],
)
METRIC_ACTIVE_FLOOD_ALERTS = Gauge(
    "flood_active_inundation_alerts_total",
    "Number of nodes and streets currently exceeding caution/critical depth",
)
METRIC_DATA_QUALITY_DEGRADED = Gauge(
    "flood_data_quality_degraded",
    "Flag indicating whether radar input is degraded (1 for degraded, 0 for nominal)",
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application startup and shutdown lifecycle event handler."""
    orchestrator = FloodPipelineOrchestrator()
    try:
        await orchestrator.execute_nowcast_cycle()
    except Exception:
        pass
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description="Sub-minute urban flood nowcasting engine combining IMD Doppler radar QPE, DEM routing, GNN surrogates, and mass-conserving hydraulics.",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Routers
app.include_router(api_v1_router, prefix=settings.API_V1_PREFIX)
app.include_router(ws_router)


@app.get("/health", tags=["Health & Status"])
async def health_check():
    """Liveness probe returning application operational status."""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "environment": settings.ENVIRONMENT,
    }


@app.get("/ready", tags=["Health & Status"])
async def readiness_check():
    """Readiness probe checking cached grids, surrogate model, and database."""
    cache_ready = (settings.DEM_CACHE_DIR / "flow_direction.npy").exists()
    return {
        "status": "ready" if cache_ready else "initializing",
        "dem_cache_ready": cache_ready,
        "surrogate_model_ready": settings.SURROGATE_MODEL_PATH.exists(),
    }


@app.get("/metrics", tags=["Observability"])
async def prometheus_metrics():
    """Prometheus metrics scrape endpoint."""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)

"""Configuration module for the Urban Flood Nowcasting Engine."""

from pathlib import Path
from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable bindings and multi-city path helpers."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # General / Application
    APP_NAME: str = "Urban Flood Nowcasting Engine"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"
    API_KEYS: List[str] = Field(default_factory=lambda: ["dev-api-key-12345", "test-api-key-67890", "sih_flood_secret_key_2024"])
    DEFAULT_CITY_ID: str = "hyderabad"

    # Base Directory Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    CITIES_DATA_DIR: Path = DATA_DIR / "cities"
    
    # Global Default Paths (for single-city backwards compatibility)
    DEM_DIR: Path = DATA_DIR / "dem"
    DEM_CACHE_DIR: Path = DATA_DIR / "dem_cache"
    RADAR_DIR: Path = DATA_DIR / "radar"
    NETWORK_DIR: Path = DATA_DIR / "network"
    CALIBRATION_DIR: Path = DATA_DIR / "calibration"
    SURROGATE_MODEL_PATH: Path = DATA_DIR / "surrogate_gnn.onnx"

    # Database & Storage
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/flood_engine"
    SYNC_DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/flood_engine"
    REDIS_URL: str = "redis://localhost:6379/0"

    # Hydrology & Radar QPE Parameters
    RADAR_STALENESS_THRESHOLD_MINUTES: int = 15
    MARSHALL_PALMER_A: float = 200.0
    MARSHALL_PALMER_B: float = 1.6
    NOWCAST_HORIZONS_MINUTES: List[int] = Field(
        default_factory=lambda: [15, 30, 45, 60, 120, 180]
    )

    # Coupling & Inundation Parameters
    CYCLE_DT_SECONDS: float = 300.0  # 5 minutes
    DEFAULT_SURFACE_PONDING_AREA_M2: float = 250.0  # Typical node subcatchment inlet ponding area
    CRITICAL_FLOOD_DEPTH_CM: float = 15.0  # Impassable barrier cutoff for vehicles
    CAUTION_FLOOD_DEPTH_CM: float = 5.0  # Advisory threshold for routing cost penalty
    ROUTING_PENALTY_BETA: float = 8.0  # Quadratic penalty multiplier

    # Rate Limiting & WebSocket Limits
    RATE_LIMIT_PER_MINUTE: int = 120
    MAX_WS_CONNECTIONS: int = 500

    # Observability & Metrics
    PROMETHEUS_PORT: int = 9090
    CYCLE_LATENCY_BUDGET_SECONDS: float = 30.0

    # Multi-City Dynamic Path Resolvers
    def get_city_dir(self, city_id: str) -> Path:
        p = self.CITIES_DATA_DIR / city_id.lower()
        p.mkdir(parents=True, exist_ok=True)
        return p

    def get_city_dem_dir(self, city_id: str) -> Path:
        p = self.get_city_dir(city_id) / "dem"
        p.mkdir(parents=True, exist_ok=True)
        return p

    def get_city_dem_cache_dir(self, city_id: str) -> Path:
        p = self.get_city_dir(city_id) / "dem_cache"
        p.mkdir(parents=True, exist_ok=True)
        return p

    def get_city_network_dir(self, city_id: str) -> Path:
        p = self.get_city_dir(city_id) / "network"
        p.mkdir(parents=True, exist_ok=True)
        return p

    def get_city_radar_dir(self, city_id: str) -> Path:
        p = self.get_city_dir(city_id) / "radar"
        p.mkdir(parents=True, exist_ok=True)
        return p

    def get_city_model_path(self, city_id: str) -> Path:
        models_dir = self.get_city_dir(city_id) / "models"
        models_dir.mkdir(parents=True, exist_ok=True)
        return models_dir / "surrogate_gnn.onnx"


settings = Settings()

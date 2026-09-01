"""City Engine Registry for Dynamic Multi-City Nowcast Execution & Lazy Loading."""

from typing import Dict, List, Optional
import threading

from src.config import settings
from src.cities import CITY_REGISTRY, CityProfile, get_city_profile
from src.workers.pipeline_worker import FloodPipelineOrchestrator


class CityEngineRegistry:
    """Thread-safe registry for dynamically loading and managing per-city nowcast engines."""

    _lock = threading.Lock()
    _engines: Dict[str, FloodPipelineOrchestrator] = {}

    @classmethod
    def get_engine(cls, city_id: str = "hyderabad") -> FloodPipelineOrchestrator:
        """Retrieves or lazy-loads the dedicated nowcast engine for a specified city."""
        city_key = city_id.strip().lower()
        profile = get_city_profile(city_key)

        with cls._lock:
            if city_key not in cls._engines:
                # Instantiate city-bound pipeline orchestrator
                engine = FloodPipelineOrchestrator(city_id=city_key)
                cls._engines[city_key] = engine
            return cls._engines[city_key]

    @classmethod
    def list_active_engines(cls) -> List[str]:
        """Returns list of currently initialized in-memory city engines."""
        with cls._lock:
            return list(cls._engines.keys())

    @classmethod
    def reset_city_engine(cls, city_id: str) -> None:
        """Flushes an in-memory city engine when new models or terrain rasters are trained."""
        city_key = city_id.strip().lower()
        with cls._lock:
            if city_key in cls._engines:
                del cls._engines[city_key]


def get_city_engine(city_id: str = "hyderabad") -> FloodPipelineOrchestrator:
    """Convenience getter for city nowcasting engine."""
    return CityEngineRegistry.get_engine(city_id)

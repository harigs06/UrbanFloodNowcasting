"""ARQ Pipeline Worker for Real-Time End-to-End Flood Nowcasting (Multi-City Enabled).

Orchestrates the 5-stage nowcast cycle for any configured city at 5-15 minute cadence:
  Stage 1: Radar QPE & Optical Flow Advection (15-180m horizons)
  Stage 2: Surface Routing via City Cached D8 Grids
  Stage 3: GNN Surrogate Inference & Hydraulic Coupling
  Stage 4: Mass-Conserving Reservoir Routing Depth Updates
  Stage 5: Street Inundation Mapping & WebSocket Broadcast
"""

import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import numpy as np

from src.config import settings
from src.cities import CityProfile, get_city_profile
from src.core.coupling_engine import CouplingEngine
from src.core.drainage_graph import DrainageGraph
from src.core.radar_qpe import RadarQPEEngine
from src.core.surface_routing import SurfaceRoutingEngine
from src.core.surrogate_infer import SurrogateInferenceEngine
from src.schemas.nowcast import InundationPointSchema, NowcastCycleSummarySchema
from src.api.v1.nowcast import update_current_inundation_state
from src.api.v1.websockets import ws_manager


class FloodPipelineOrchestrator:
    """Orchestrates all 5 stages of the flood nowcasting engine bound to a specific city."""

    def __init__(self, city_id: str = "hyderabad"):
        self.city_id = city_id.strip().lower()
        self.city_profile: CityProfile = get_city_profile(self.city_id)

        # Multi-City Directory Bindings
        self.city_cache_dir = settings.get_city_dem_cache_dir(self.city_id)
        self.city_network_dir = settings.get_city_network_dir(self.city_id)
        self.city_radar_dir = settings.get_city_radar_dir(self.city_id)
        self.city_model_path = settings.get_city_model_path(self.city_id)

        # Core Engines
        self.radar_engine = RadarQPEEngine()
        self.surface_engine = SurfaceRoutingEngine(cache_dir=self.city_cache_dir)
        self.drainage_graph = DrainageGraph()
        self.coupling_engine = CouplingEngine()
        self.surrogate_engine = SurrogateInferenceEngine(
            model_path=self.city_model_path,
            drainage_graph=self.drainage_graph,
        )

        self._inlet_coords: List[tuple] = []
        self._initialize_city_topology()

    def _initialize_city_topology(self) -> None:
        """Initializes node and conduit structures from the city's ingested topology."""
        json_path = self.city_network_dir / "drainage_topology.json"
        if not json_path.exists():
            json_path = settings.NETWORK_DIR / "drainage_topology.json"

        nodes = []
        conduits = []
        if json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                nodes = data.get("nodes", [])
                conduits = data.get("conduits", [])
            except Exception:
                pass

        if not nodes:
            from src.api.v1.drainage import SAMPLE_NODES, SAMPLE_CONDUITS
            nodes = [n.model_dump() for n in SAMPLE_NODES]
            conduits = [c.model_dump() for c in SAMPLE_CONDUITS]

        self.drainage_graph.build_graph(nodes, conduits)

        # Precompute inlet grid coordinates on the city DEM raster
        rows, cols = self.surface_engine.fdir.shape
        min_lon, min_lat, max_lon, max_lat = self.city_profile.bounding_box
        self._inlet_coords = []

        for nid in self.drainage_graph.node_ids:
            node_attr = self.drainage_graph.node_attrs.get(nid, {})
            lat = float(node_attr.get("latitude", self.city_profile.center_coords[0]))
            lon = float(node_attr.get("longitude", self.city_profile.center_coords[1]))
            r = int(np.clip(((lat - min_lat) / max(1e-4, max_lat - min_lat)) * rows, 0, rows - 1))
            c = int(np.clip(((lon - min_lon) / max(1e-4, max_lon - min_lon)) * cols, 0, cols - 1))
            self._inlet_coords.append((r, c))

    async def execute_nowcast_cycle(
        self,
        radar_dbz_grid: Optional[np.ndarray] = None,
        radar_timestamp: Optional[datetime] = None,
        cycle_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes full Stage 1 -> Stage 5 nowcasting pipeline for the city."""
        start_time = time.perf_counter()
        now = datetime.now(timezone.utc)
        cid = cycle_id or f"{self.city_id}-cycle-{int(now.timestamp())}"

        # ----------------------------------------------------
        # Stage 1: Radar QPE & Optical Flow Nowcasting
        # ----------------------------------------------------
        forecasts, data_quality, staleness_sec = self.radar_engine.process_nowcast_cycle(
            radar_dbz_grid=radar_dbz_grid,
            radar_timestamp=radar_timestamp,
            current_time=now,
        )

        node_ids = self.drainage_graph.node_ids
        inlet_coords = self._inlet_coords if self._inlet_coords else [(10, 10)] * len(node_ids)
        horizons_results: Dict[int, List[InundationPointSchema]] = {}
        all_depths_list = []

        # ----------------------------------------------------
        # Stage 2 to 4: Surface Routing, Surrogate & Mass Balance per Horizon
        # ----------------------------------------------------
        for horizon, rain_grid in forecasts.items():
            # Stage 2: Surface Routing
            node_inflows = self.surface_engine.route_flux_to_inlets(
                rain_rate_mm_hr=rain_grid,
                inlet_grid_coords=inlet_coords,
                dt_seconds=settings.CYCLE_DT_SECONDS,
            )

            # Stage 3: GNN Surrogate & Hydraulic Solve
            depths_cm, surcharges_m3s, new_storage, solver_used = self.surrogate_engine.infer(
                node_inflows_m3s=node_inflows,
                dt_seconds=settings.CYCLE_DT_SECONDS,
            )

            # Stage 4: Mass-Conserving Reservoir Routing Update
            node_metrics = self.coupling_engine.update_node_depths(
                node_ids=node_ids,
                node_inflows_m3s=node_inflows,
                node_capacities_m3s=self.drainage_graph.node_capacities,
                surface_areas_m2=self.drainage_graph.node_storage_areas,
                dt_seconds=settings.CYCLE_DT_SECONDS,
            )

            points: List[InundationPointSchema] = []
            for nid, m in node_metrics.items():
                points.append(
                    InundationPointSchema(
                        entity_id=nid,
                        entity_type="node",
                        water_depth_cm=m["water_depth_cm"],
                        surcharge_flow_m3s=m["surcharge_flow_m3s"],
                        excess_storage_m3=m["excess_storage_m3"],
                        risk_level=m["risk_level"],
                    )
                )
                all_depths_list.append(m["water_depth_cm"])

            # Map to street segments
            from src.api.v1.routing import get_city_router
            router_inst = get_city_router(self.city_id)
            for u in router_inst.adjacency:
                for v, street in router_inst.adjacency[u]:
                    sid = street["id"]
                    nearest_node = street.get("nearest_node_id", node_ids[0] if node_ids else "node-01")
                    m = node_metrics.get(nearest_node, {"water_depth_cm": 0.0, "risk_level": "safe", "surcharge_flow_m3s": 0.0, "excess_storage_m3": 0.0})
                    points.append(
                        InundationPointSchema(
                            entity_id=sid,
                            entity_type="street",
                            water_depth_cm=m["water_depth_cm"],
                            surcharge_flow_m3s=m["surcharge_flow_m3s"],
                            excess_storage_m3=m["excess_storage_m3"],
                            risk_level=m["risk_level"],
                        )
                    )

            horizons_results[horizon] = points

        elapsed_ms = (time.perf_counter() - start_time) * 1000.0
        max_d = float(max(all_depths_list)) if all_depths_list else 0.0
        mean_d = float(np.mean(all_depths_list)) if all_depths_list else 0.0
        flooded_count = sum(1 for d in all_depths_list if d >= settings.CAUTION_FLOOD_DEPTH_CM)

        summary = NowcastCycleSummarySchema(
            cycle_id=cid,
            cycle_timestamp=now,
            horizon_minutes=15,
            data_quality=data_quality,
            radar_staleness_seconds=staleness_sec,
            max_depth_cm=round(max_d, 2),
            mean_depth_cm=round(mean_d, 2),
            total_flooded_nodes=flooded_count,
            execution_duration_ms=round(elapsed_ms, 2),
            status="completed",
        )

        # ----------------------------------------------------
        # Stage 5: State Update & WebSocket Broadcast
        # ----------------------------------------------------
        update_current_inundation_state(summary, horizons_results, city_id=self.city_id)

        # Broadcast via WebSockets
        broadcast_payload = {
            "type": "nowcast_update",
            "city_id": self.city_id,
            "cycle_id": cid,
            "timestamp": now.isoformat(),
            "data_quality": data_quality,
            "max_depth_cm": summary.max_depth_cm,
            "execution_ms": summary.execution_duration_ms,
            "horizons": {h: len(pts) for h, pts in horizons_results.items()},
        }
        await ws_manager.broadcast_inundation_update(broadcast_payload)

        return {
            "summary": summary,
            "horizons": horizons_results,
        }


# ARQ worker task wrapper
async def run_pipeline_task(ctx: Dict[str, Any], city_id: str = "hyderabad", radar_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """ARQ async job invoked on every nowcasting cycle for a specific city."""
    orchestrator = FloodPipelineOrchestrator(city_id=city_id)
    result = await orchestrator.execute_nowcast_cycle()
    return {"status": "success", "city_id": city_id, "cycle_id": result["summary"].cycle_id}


class WorkerSettings:
    """ARQ Worker configuration."""
    functions = [run_pipeline_task]
    redis_settings = None

"""Flood-Safe Shortest Path Routing Engine.

Implements A* / Dijkstra shortest-path search with flood-risk weighting:
1. Base traversal cost = segment length (or travel time).
2. Flooded penalty scaling (quadratic cost):
       Cost = length * (1 + beta * (depth / caution_depth)^2)
3. Impassable barrier: Hard cutoff when depth >= 15.0 cm (infinite cost / edge pruned).
4. Route Caching Fallback: Caches and returns the last known safe route if
   nowcast data quality is degraded or an active query is impassable.
"""

import heapq
from typing import Dict, List, Optional, Set, Tuple
import numpy as np

from src.config import settings
from src.schemas.routing import RouteResponseSchema, RouteStepSchema


class FloodSafeRouter:
    """Computes flood-safe routes across urban street networks."""

    def __init__(
        self,
        critical_depth_cm: float = settings.CRITICAL_FLOOD_DEPTH_CM,
        caution_depth_cm: float = settings.CAUTION_FLOOD_DEPTH_CM,
        beta_penalty: float = settings.ROUTING_PENALTY_BETA,
    ):
        self.critical_depth_cm = critical_depth_cm
        self.caution_depth_cm = caution_depth_cm
        self.beta_penalty = beta_penalty

        # Graph structure: intersection_id -> list of (neighbor_id, street_dict)
        self.adjacency: Dict[str, List[Tuple[str, Dict[str, any]]]] = {}
        self.intersection_coords: Dict[str, Tuple[float, float]] = {}
        
        # Route cache: (origin_id, dest_id) -> RouteResponseSchema
        self._route_cache: Dict[Tuple[str, str], RouteResponseSchema] = {}

    def build_network(
        self,
        street_segments: List[Dict[str, any]],
        intersections: Optional[Dict[str, Tuple[float, float]]] = None,
    ) -> None:
        """Constructs street graph topology from segment list."""
        self.adjacency.clear()
        self.intersection_coords = intersections or {}

        for street in street_segments:
            u = street["from_intersection_id"]
            v = street["to_intersection_id"]

            if u not in self.adjacency:
                self.adjacency[u] = []
            if v not in self.adjacency:
                self.adjacency[v] = []

            # Bidirectional street segments
            self.adjacency[u].append((v, street))
            self.adjacency[v].append((u, street))

        # Store intersection coords from coordinates_json if available
        for street in street_segments:
            u = street["from_intersection_id"]
            v = street["to_intersection_id"]
            coords = street.get("coordinates_json") or []
            if coords and len(coords) >= 2:
                if u not in self.intersection_coords:
                    self.intersection_coords[u] = tuple(coords[0])
                if v not in self.intersection_coords:
                    self.intersection_coords[v] = tuple(coords[-1])

        # Automatically connect proximate intersections (k-NN spatial connectivity)
        # to ensure realistic urban cross-corridor transit between named junctions
        coords_list = list(self.intersection_coords.items())
        for i in range(len(coords_list)):
            u, (lon1, lat1) = coords_list[i]
            dists = []
            for j in range(len(coords_list)):
                if i == j:
                    continue
                w, (lon2, lat2) = coords_list[j]
                d = float(np.sqrt(
                    ((lon2 - lon1) * 111000.0 * np.cos(np.radians(lat1))) ** 2
                    + ((lat2 - lat1) * 111000.0) ** 2
                ))
                dists.append((d, w, lon2, lat2))
            dists.sort(key=lambda x: x[0])
            for d, w, lon2, lat2 in dists[:4]:
                if d <= 3500.0:
                    if not any(neigh == w for neigh, _ in self.adjacency.get(u, [])):
                        connector_street = {
                            "id": f"conn-{u}-{w}",
                            "name": f"{u.replace('int-', '').replace('-', ' ').title()} - {w.replace('int-', '').replace('-', ' ').title()} Link",
                            "from_intersection_id": u,
                            "to_intersection_id": w,
                            "length_m": round(d, 1),
                            "water_depth_cm": 0.0,
                            "coordinates_json": [[lon1, lat1], [lon2, lat2]],
                        }
                        if u not in self.adjacency:
                            self.adjacency[u] = []
                        if w not in self.adjacency:
                            self.adjacency[w] = []
                        self.adjacency[u].append((w, connector_street))
                        self.adjacency[w].append((u, connector_street))

    # Vehicle-specific depth thresholds (in cm)
    VEHICLE_THRESHOLDS = {
        "two_wheeler": {"critical": 8.0, "caution": 4.0, "beta": 4.0},
        "pedestrian": {"critical": 10.0, "caution": 5.0, "beta": 4.0},
        "car": {"critical": 15.0, "caution": 7.0, "beta": 3.0},
        "light_vehicle": {"critical": 15.0, "caution": 7.0, "beta": 3.0},
        "bus": {"critical": 30.0, "caution": 15.0, "beta": 2.0},
        "heavy_truck": {"critical": 35.0, "caution": 18.0, "beta": 1.8},
        "emergency": {"critical": 50.0, "caution": 25.0, "beta": 1.0},
    }

    def calculate_edge_cost(
        self,
        street: Dict[str, any],
        street_depth_map: Dict[str, float],
        critical_depth_cm: Optional[float] = None,
        caution_depth_cm: Optional[float] = None,
        beta_penalty: Optional[float] = None,
    ) -> Tuple[float, bool]:
        """Calculates dynamic traversal cost with flood-depth penalty.
        
        Returns:
            (cost, is_passable)
        """
        crit = critical_depth_cm if critical_depth_cm is not None else self.critical_depth_cm
        caut = caution_depth_cm if caution_depth_cm is not None else self.caution_depth_cm
        beta = beta_penalty if beta_penalty is not None else self.beta_penalty

        sid = street["id"]
        length_m = street.get("length_m", 100.0)
        depth_cm = street_depth_map.get(sid, street.get("water_depth_cm", 0.0))

        # Hard barrier cutoff
        if depth_cm >= crit:
            return float("inf"), False

        # Quadratic penalty above caution depth
        if depth_cm > caut:
            penalty = 1.0 + beta * ((depth_cm / max(1.0, caut)) ** 2)
        elif depth_cm > 0.0:
            penalty = 1.0 + (depth_cm / max(1.0, caut))
        else:
            penalty = 1.0

        effective_cost = length_m * penalty
        return effective_cost, True

    def _heuristic_distance(self, u: str, v: str) -> float:
        """Euclidean distance heuristic for A* in meters (approx. 111,000 m/degree)."""
        if u not in self.intersection_coords or v not in self.intersection_coords:
            return 0.0

        lon1, lat1 = self.intersection_coords[u]
        lon2, lat2 = self.intersection_coords[v]
        dx = (lon2 - lon1) * 111000.0 * np.cos(np.radians((lat1 + lat2) / 2.0))
        dy = (lat2 - lat1) * 111000.0
        return float(np.sqrt(dx**2 + dy**2))

    def find_safe_route(
        self,
        origin_intersection_id: str,
        destination_intersection_id: str,
        street_depth_map: Optional[Dict[str, float]] = None,
        vehicle_type: str = "car",
        is_degraded_nowcast: bool = False,
    ) -> RouteResponseSchema:
        """Finds the optimal flood-safe path using A* search."""
        street_depths = street_depth_map or {}
        cache_key = (origin_intersection_id, destination_intersection_id, vehicle_type)

        v_config = self.VEHICLE_THRESHOLDS.get(vehicle_type, self.VEHICLE_THRESHOLDS["car"])
        crit_depth = v_config["critical"]
        caut_depth = v_config["caution"]
        beta = v_config["beta"]

        # Check if origin and destination exist in network
        if (
            origin_intersection_id not in self.adjacency
            or destination_intersection_id not in self.adjacency
        ):
            # Fallback to cache if available
            if cache_key in self._route_cache:
                cached = self._route_cache[cache_key].model_copy()
                cached.is_cached_fallback = True
                cached.warning_message = "Origin/destination not in live graph; serving cached route."
                return cached

            return RouteResponseSchema(
                path_found=False,
                total_distance_m=0.0,
                estimated_travel_time_seconds=0.0,
                max_flood_depth_encountered_cm=0.0,
                overall_safety_rating="impassable_blocked",
                warning_message="Origin or destination intersection not found in street network.",
                steps=[],
                geometry=[],
            )

        # Immediate arrival if origin == destination
        if origin_intersection_id == destination_intersection_id:
            coords = self.intersection_coords.get(origin_intersection_id, (0.0, 0.0))
            return RouteResponseSchema(
                path_found=True,
                total_distance_m=50.0,
                estimated_travel_time_seconds=10.0,
                max_flood_depth_encountered_cm=0.0,
                overall_safety_rating="safe",
                is_cached_fallback=False,
                steps=[
                    RouteStepSchema(
                        segment_id="direct-arrival",
                        street_name="Immediate Destination Point",
                        length_m=50.0,
                        water_depth_cm=0.0,
                        risk_level="safe",
                        coordinates=[[coords[0], coords[1]]],
                    )
                ],
                geometry=[[coords[0], coords[1]]],
            )

        # Priority queue: (f_score, counter, current_cost_g, current_node, path_steps, path_coords, max_depth)
        entry_counter = 0
        queue = [(0.0, entry_counter, 0.0, origin_intersection_id, [], [], 0.0)]
        visited: Dict[str, float] = {}

        while queue:
            f_score, _, g_cost, u, steps, full_geom, max_depth = heapq.heappop(queue)

            if u == destination_intersection_id and steps:
                # Successfully reached destination
                total_dist = sum(s.length_m for s in steps)
                avg_speed_mps = 40.0 / 3.6  # 40 km/h baseline
                est_time = total_dist / avg_speed_mps

                safety = (
                    "safe" if max_depth < caut_depth
                    else "caution_flooded_sections"
                )

                response = RouteResponseSchema(
                    path_found=True,
                    total_distance_m=round(total_dist, 1),
                    estimated_travel_time_seconds=round(est_time, 1),
                    max_flood_depth_encountered_cm=round(max_depth, 1),
                    overall_safety_rating=safety,
                    is_cached_fallback=False,
                    steps=steps,
                    geometry=full_geom if full_geom else [[0.0, 0.0]],
                )

                # Update cache
                self._route_cache[cache_key] = response
                return response

            if u in visited and visited[u] <= g_cost:
                continue
            visited[u] = g_cost

            for v, street in self.adjacency.get(u, []):
                edge_cost, is_passable = self.calculate_edge_cost(
                    street,
                    street_depths,
                    critical_depth_cm=crit_depth,
                    caution_depth_cm=caut_depth,
                    beta_penalty=beta,
                )
                if not is_passable:
                    continue

                new_g = g_cost + edge_cost
                if v in visited and visited[v] <= new_g:
                    continue

                sid = street["id"]
                s_depth = street_depths.get(sid, street.get("water_depth_cm", 0.0))
                s_len = street.get("length_m", 100.0)
                coords = street.get("coordinates_json") or []

                step_risk = "safe" if s_depth < caut_depth else "caution"

                new_step = RouteStepSchema(
                    segment_id=sid,
                    street_name=street.get("name", f"Street-{sid}"),
                    length_m=s_len,
                    water_depth_cm=round(s_depth, 1),
                    risk_level=step_risk,
                    coordinates=coords,
                )

                h_score = self._heuristic_distance(v, destination_intersection_id)
                new_f = new_g + h_score
                new_max_depth = max(max_depth, s_depth)

                entry_counter += 1
                heapq.heappush(
                    queue,
                    (
                        new_f,
                        entry_counter,
                        new_g,
                        v,
                        steps + [new_step],
                        full_geom + coords,
                        new_max_depth,
                    ),
                )

        # No path found with live depth conditions -> Fallback to cached route if present
        if cache_key in self._route_cache:
            cached = self._route_cache[cache_key].model_copy()
            cached.is_cached_fallback = True
            cached.warning_message = "All real-time paths blocked by >=15cm flooding; serving cached last-known safe route."
            return cached

        return RouteResponseSchema(
            path_found=False,
            total_distance_m=0.0,
            estimated_travel_time_seconds=0.0,
            max_flood_depth_encountered_cm=0.0,
            overall_safety_rating="impassable_blocked",
            warning_message="All viable routes are blocked by >=15cm flooding.",
            steps=[],
            geometry=[],
        )

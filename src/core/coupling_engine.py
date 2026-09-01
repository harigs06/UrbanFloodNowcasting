"""Coupling Engine and Mass-Conserving Reservoir Routing Depth Updates.

Implements the mass-conserving reservoir routing depth update across cycles:
    S(t+1) = S(t) + (Q_in - Q_out_capacity) * dt          # Excess storage balance
    h_street(t+1) = max(0, S(t+1)) / A_surface * 100      # cm, mass-conserving

Maintains persistent storage state S(t) across cycles to accurately model
drainage-down dynamics between storm pulses.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np

from src.config import settings


class CouplingEngine:
    """Couples surface inflows and drainage network capacity via mass-conserving reservoir routing."""

    def __init__(self):
        # Persistent storage state across cycles: node_id -> excess_storage_m3
        self._node_storage_state: Dict[str, float] = {}
        self._node_depth_state: Dict[str, float] = {}

    def get_state(self, node_id: str) -> Tuple[float, float]:
        """Returns (storage_m3, depth_cm) for a given node."""
        return (
            self._node_storage_state.get(node_id, 0.0),
            self._node_depth_state.get(node_id, 0.0),
        )

    def set_state(self, node_id: str, storage_m3: float, depth_cm: float) -> None:
        """Sets persistent storage state for a node."""
        self._node_storage_state[node_id] = max(0.0, float(storage_m3))
        self._node_depth_state[node_id] = max(0.0, float(depth_cm))

    def reset_state(self) -> None:
        """Clears all accumulated storage state (e.g. for testing or fresh start)."""
        self._node_storage_state.clear()
        self._node_depth_state.clear()

    def update_node_depths(
        self,
        node_ids: List[str],
        node_inflows_m3s: np.ndarray,
        node_capacities_m3s: np.ndarray,
        surface_areas_m2: np.ndarray,
        dt_seconds: float = settings.CYCLE_DT_SECONDS,
    ) -> Dict[str, Dict[str, float]]:
        """Performs mass-conserving reservoir-routing depth update for all nodes.
        
        Args:
            node_ids: list of node identifiers.
            node_inflows_m3s: incoming surface runoff flux Q_in (m^3/s).
            node_capacities_m3s: stormwater conduit conveyance capacity Q_out (m^3/s).
            surface_areas_m2: ponding subcatchment area A_surface (m^2).
            dt_seconds: time elapsed since previous cycle.
            
        Returns:
            Dictionary mapping node_id -> metrics dict (depth_cm, storage_m3, surcharge_m3s, risk_level).
        """
        results = {}
        num_nodes = len(node_ids)

        for i in range(num_nodes):
            nid = node_ids[i]
            q_in = float(node_inflows_m3s[i])
            q_cap = float(node_capacities_m3s[i])
            area = float(surface_areas_m2[i]) if surface_areas_m2[i] > 0 else settings.DEFAULT_SURFACE_PONDING_AREA_M2

            prev_s = self._node_storage_state.get(nid, 0.0)

            # Mass conservation reservoir routing equation:
            # S(t+1) = max(0, S(t) + (Q_in - Q_out_capacity) * dt)
            net_flux = q_in - q_cap
            new_s = max(0.0, prev_s + net_flux * dt_seconds)

            # Water depth in centimeters
            depth_cm = (new_s / area) * 100.0

            # Surcharge rate (m^3/s) occurring when inflow exceeds capacity
            surcharge_rate = max(0.0, q_in - q_cap)

            # Risk classification
            if depth_cm >= settings.CRITICAL_FLOOD_DEPTH_CM:
                risk_level = "impassable"
            elif depth_cm >= settings.CAUTION_FLOOD_DEPTH_CM:
                risk_level = "caution"
            else:
                risk_level = "safe"

            # Update persistent state
            self._node_storage_state[nid] = new_s
            self._node_depth_state[nid] = depth_cm

            results[nid] = {
                "water_depth_cm": round(depth_cm, 2),
                "excess_storage_m3": round(new_s, 3),
                "surcharge_flow_m3s": round(surcharge_rate, 4),
                "risk_level": risk_level,
            }

        return results

    def map_node_depths_to_streets(
        self,
        street_segments: List[Dict[str, any]],
        node_depth_results: Dict[str, Dict[str, float]],
    ) -> List[Dict[str, any]]:
        """Maps computed node inundation depths to corresponding street segments."""
        street_results = []

        for street in street_segments:
            sid = street["id"]
            node_id = street.get("nearest_node_id")

            if node_id and node_id in node_depth_results:
                node_data = node_depth_results[node_id]
                depth_cm = node_data["water_depth_cm"]
                risk_level = node_data["risk_level"]
                surcharge = node_data["surcharge_flow_m3s"]
                storage = node_data["excess_storage_m3"]
            else:
                depth_cm = 0.0
                risk_level = "safe"
                surcharge = 0.0
                storage = 0.0

            street_results.append({
                "street_id": sid,
                "street_name": street.get("name", f"Street-{sid}"),
                "nearest_node_id": node_id,
                "water_depth_cm": depth_cm,
                "risk_level": risk_level,
                "surcharge_flow_m3s": surcharge,
                "excess_storage_m3": storage,
                "length_m": street.get("length_m", 100.0),
                "coordinates": street.get("coordinates_json", []),
            })

        return street_results

"""High-performance Drainage Network Graph and Manning Hydraulic Fallback Solver.

Uses igraph for sub-millisecond graph traversal at metropolitan scale (50,000+ nodes).
Includes the Manning's full-pipe equation solver for degraded-mode hydraulic fallback.
"""

from typing import Any, Dict, List, Optional, Tuple
import numpy as np

try:
    import igraph as ig
except ImportError:
    ig = None

from src.config import settings


class DrainageGraph:
    """Manages drainage topology and performs fast hydraulic capacity evaluations."""

    def __init__(self):
        self.node_ids: List[str] = []
        self.node_index_map: Dict[str, int] = {}
        self.node_attrs: Dict[str, Dict[str, Any]] = {}
        self.conduit_attrs: Dict[str, Dict[str, Any]] = {}
        
        # Internal adjacency matrix (num_nodes, num_nodes)
        self.adj_matrix: Optional[np.ndarray] = None
        self.node_capacities: Optional[np.ndarray] = None
        self.node_storage_areas: Optional[np.ndarray] = None
        self.ig_graph: Optional[Any] = None

    def build_graph(
        self,
        nodes: List[Dict[str, Any]],
        conduits: List[Dict[str, Any]],
    ) -> None:
        """Constructs igraph topology and caches structural matrices."""
        self.node_ids = [n["id"] for n in nodes]
        self.node_index_map = {nid: i for i, nid in enumerate(self.node_ids)}
        self.node_attrs = {n["id"]: n for n in nodes}
        self.conduit_attrs = {c["id"]: c for c in conduits}

        num_nodes = len(self.node_ids)
        self.adj_matrix = np.zeros((num_nodes, num_nodes), dtype=np.float32)
        self.node_capacities = np.zeros(num_nodes, dtype=np.float32)
        self.node_storage_areas = np.array(
            [n.get("surface_area_m2", settings.DEFAULT_SURFACE_PONDING_AREA_M2) for n in nodes],
            dtype=np.float32,
        )

        edges = []
        edge_capacities = []

        for c in conduits:
            from_id = c["from_node_id"]
            to_id = c["to_node_id"]
            if from_id in self.node_index_map and to_id in self.node_index_map:
                u = self.node_index_map[from_id]
                v = self.node_index_map[to_id]
                
                # Calculate full pipe capacity via Manning equation
                cap = self.compute_manning_full_capacity(
                    diameter_m=c["diameter_m"],
                    slope=c.get("slope", 0.005),
                    roughness=c.get("roughness", 0.015),
                    shape=c.get("shape", "circular"),
                    width_m=c.get("width_m"),
                )
                c["full_capacity_m3s"] = cap
                
                self.adj_matrix[u, v] = 1.0
                self.node_capacities[u] += cap
                edges.append((u, v))
                edge_capacities.append(cap)

        # For outfalls without downstream pipes, assign high nominal outfall capacity
        for i, n in enumerate(nodes):
            if n.get("is_outfall", False) or self.node_capacities[i] == 0:
                self.node_capacities[i] = max(self.node_capacities[i], 10.0)

        # Construct igraph instance if available
        if ig is not None:
            self.ig_graph = ig.Graph(n=num_nodes, edges=edges, directed=True)
            self.ig_graph.vs["name"] = self.node_ids
            self.ig_graph.es["capacity"] = edge_capacities

    @staticmethod
    def compute_manning_full_capacity(
        diameter_m: float,
        slope: float,
        roughness: float = 0.015,
        shape: str = "circular",
        width_m: Optional[float] = None,
    ) -> float:
        """Calculates pipe full-flow capacity using Manning's equation.
        
        Formula:
            Q_full = (1 / n) * A * (R_h)^(2/3) * S^(1/2)
            Circular: A = pi * D^2 / 4, R_h = D / 4
            Rectangular: A = W * D, R_h = (W * D) / (2W + 2D)
        """
        slope_pos = max(1e-4, abs(slope))
        n_safe = max(1e-3, roughness)

        if shape == "circular" or width_m is None:
            d = max(0.1, diameter_m)
            area = (np.pi * (d ** 2)) / 4.0
            r_h = d / 4.0
        else:
            w = max(0.1, width_m)
            d = max(0.1, diameter_m)
            area = w * d
            r_h = area / (2.0 * w + 2.0 * d)

        q_full = (1.0 / n_safe) * area * (r_h ** (2.0 / 3.0)) * np.sqrt(slope_pos)
        return float(q_full)

    def solve_manning_fallback(
        self,
        node_inflows: np.ndarray,
        prev_storage: Optional[np.ndarray] = None,
        dt_seconds: float = settings.CYCLE_DT_SECONDS,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Fast Manning-based hydraulic approximation fallback when GNN is bypassed.
        
        Returns:
            (node_depths_cm, surcharge_flow_m3s, new_storage_m3)
        """
        num_nodes = len(self.node_ids)
        if prev_storage is None:
            prev_storage = np.zeros(num_nodes, dtype=np.float32)

        capacities = self.node_capacities if self.node_capacities is not None else np.full(num_nodes, 1.0)
        areas = self.node_storage_areas if self.node_storage_areas is not None else np.full(num_nodes, 250.0)

        # Surcharge flux when inflow exceeds conveyance capacity
        surcharge_flow = np.maximum(0.0, node_inflows - capacities)
        
        # Mass balance reservoir update: S(t+1) = max(0, S(t) + (Q_in - Q_cap) * dt)
        net_flux = node_inflows - capacities
        new_storage = np.maximum(0.0, prev_storage + net_flux * dt_seconds)
        
        # Street surface inundation depth: h = max(0, S) / Area * 100 (cm)
        depths_cm = (new_storage / areas) * 100.0

        return depths_cm.astype(np.float32), surcharge_flow.astype(np.float32), new_storage.astype(np.float32)

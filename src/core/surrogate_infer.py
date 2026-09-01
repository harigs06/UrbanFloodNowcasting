"""ONNX Runtime GNN Surrogate Inference Engine.

Executes the PyG-trained GNN surrogate model in single-digit milliseconds,
predicting nodal water depth and surcharge rates at city scale.
Falls back to the Manning solver in `drainage_graph.py` if the ONNX model is missing or disabled.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
import numpy as np
import onnxruntime as ort

from src.config import settings
from src.core.drainage_graph import DrainageGraph


class SurrogateInferenceEngine:
    """Ultra-fast ONNX surrogate inference runner with graceful hydraulic fallback."""

    def __init__(
        self,
        model_path: Optional[Path] = None,
        drainage_graph: Optional[DrainageGraph] = None,
    ):
        self.model_path = model_path or settings.SURROGATE_MODEL_PATH
        self.drainage_graph = drainage_graph or DrainageGraph()
        self.session: Optional[ort.InferenceSession] = None
        self._initialize_session()

    def _initialize_session(self) -> None:
        """Initializes the ONNX runtime inference session or generates surrogate if missing."""
        try:
            if not self.model_path.exists():
                # Auto-train and export initial baseline model if absent
                from src.offline.gnn_training import GNNTrainer
                trainer = GNNTrainer(model_save_path=self.model_path)
                trainer.train_and_export(epochs=5, num_nodes=20)

            # Create ONNX session with CPU execution provider and optimization
            opts = ort.SessionOptions()
            opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
            opts.intra_op_num_threads = 2
            
            self.session = ort.InferenceSession(
                str(self.model_path),
                sess_options=opts,
                providers=["CPUExecutionProvider"],
            )
        except Exception as exc:
            # Degraded fallback mode
            self.session = None

    def infer(
        self,
        node_inflows_m3s: np.ndarray,
        prev_depths_cm: Optional[np.ndarray] = None,
        prev_storage_m3: Optional[np.ndarray] = None,
        dt_seconds: float = settings.CYCLE_DT_SECONDS,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, str]:
        """Runs GNN inference or Manning fallback.
        
        Args:
            node_inflows_m3s: 1D array of inflow rates Q_in (m^3/s).
            prev_depths_cm: 1D array of prior water depths.
            prev_storage_m3: 1D array of prior excess storage.
            dt_seconds: cycle interval in seconds.
            
        Returns:
            (predicted_depths_cm, surcharge_m3s, new_storage_m3, solver_used)
        """
        num_nodes = len(node_inflows_m3s)
        if prev_depths_cm is None:
            prev_depths_cm = np.zeros(num_nodes, dtype=np.float32)
        if prev_storage_m3 is None:
            prev_storage_m3 = np.zeros(num_nodes, dtype=np.float32)

        # 1. Try ONNX GNN Surrogate
        if self.session is not None:
            try:
                # Prepare node feature matrix: [inflow, prev_depth, const_slope, storage_area_norm]
                storage_areas = (
                    self.drainage_graph.node_storage_areas
                    if self.drainage_graph.node_storage_areas is not None and len(self.drainage_graph.node_storage_areas) == num_nodes
                    else np.full(num_nodes, 250.0, dtype=np.float32)
                )
                
                features = np.column_stack([
                    node_inflows_m3s,
                    prev_depths_cm,
                    np.full(num_nodes, 0.01, dtype=np.float32),
                    storage_areas / 500.0,
                ]).astype(np.float32)[np.newaxis, ...]  # Batch shape (1, num_nodes, 4)

                adj = (
                    self.drainage_graph.adj_matrix
                    if self.drainage_graph.adj_matrix is not None and self.drainage_graph.adj_matrix.shape == (num_nodes, num_nodes)
                    else np.eye(num_nodes, dtype=np.float32)
                )

                inputs = {
                    "node_features": features,
                    "adjacency_matrix": adj,
                }

                outputs = self.session.run(None, inputs)
                pred_depths = np.squeeze(outputs[0], axis=0).astype(np.float32)
                pred_surcharges = np.squeeze(outputs[1], axis=0).astype(np.float32)

                # Update storage from depth: S = (depth_cm / 100) * Area
                new_storage = (pred_depths / 100.0) * storage_areas

                return pred_depths, pred_surcharges, new_storage, "gnn_surrogate"
            except Exception:
                pass  # Fall through to Manning fallback

        # 2. Degraded Manning Hydraulic Fallback
        depths, surcharges, storage = self.drainage_graph.solve_manning_fallback(
            node_inflows=node_inflows_m3s,
            prev_storage=prev_storage_m3,
            dt_seconds=dt_seconds,
        )
        return depths, surcharges, storage, "manning_fallback"

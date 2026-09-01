"""Unit tests for Drainage Network Hydraulics and Manning Full-Pipe Solvers."""

import numpy as np
import pytest

from src.core.drainage_graph import DrainageGraph
from src.core.surrogate_infer import SurrogateInferenceEngine


def test_manning_equation_calculation():
    """Validates Manning pipe capacity calculation against analytical formula."""
    # Q = (1/n) * A * R^(2/3) * S^(1/2)
    # Circular pipe: D = 1.0m -> A = pi/4 = 0.7854 m^2, R = D/4 = 0.25m, R^(2/3) = 0.39685
    # n = 0.015, S = 0.01 -> S^(1/2) = 0.1
    # Q = (1 / 0.015) * 0.7854 * 0.39685 * 0.1 = 66.67 * 0.03117 = 2.078 m^3/s
    cap = DrainageGraph.compute_manning_full_capacity(
        diameter_m=1.0,
        slope=0.01,
        roughness=0.015,
        shape="circular",
    )
    assert 2.0 <= cap <= 2.2


def test_drainage_graph_surcharge_resolution(sample_drainage_graph):
    """Verifies that inflow exceeding pipe capacity correctly registers as surcharge flow."""
    # Under low inflow (0.5 m^3/s < capacity), surcharge should be zero
    inflows_low = np.array([0.5, 0.5, 0.5, 0.5], dtype=np.float32)
    depths, surcharges, storage = sample_drainage_graph.solve_manning_fallback(inflows_low)
    assert np.all(surcharges == 0.0)
    assert np.all(depths == 0.0)

    # Under high storm inflow (10.0 m^3/s > capacity), surcharge and depth increase
    inflows_high = np.array([10.0, 10.0, 10.0, 10.0], dtype=np.float32)
    depths, surcharges, storage = sample_drainage_graph.solve_manning_fallback(inflows_high, dt_seconds=300.0)
    assert np.any(surcharges > 0.0)
    assert np.any(depths > 0.0)
    assert np.any(storage > 0.0)


def test_surrogate_inference_execution(sample_drainage_graph):
    """Tests the ONNX surrogate inference runner and output dimensions."""
    engine = SurrogateInferenceEngine(drainage_graph=sample_drainage_graph)
    inflows = np.array([1.2, 2.5, 0.8, 3.0], dtype=np.float32)

    depths, surcharges, storage, solver = engine.infer(
        node_inflows_m3s=inflows,
        dt_seconds=300.0,
    )

    assert len(depths) == 4
    assert len(surcharges) == 4
    assert len(storage) == 4
    assert np.all(depths >= 0.0)
    assert np.all(surcharges >= 0.0)
    assert solver in ["gnn_surrogate", "manning_fallback"]

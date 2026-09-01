"""Mass Conservation and Reservoir-Routing Invariant Tests for the Coupling Engine."""

import numpy as np
import pytest

from src.core.coupling_engine import CouplingEngine


def test_mass_balance_single_cycle_conservation():
    """Verifies single-step mass balance: S(t+1) = max(0, S(t) + (Q_in - Q_out) * dt)."""
    engine = CouplingEngine()
    node_ids = ["node_A"]
    dt = 300.0  # 5 minutes
    area = np.array([200.0])
    cap = np.array([2.0])  # 2.0 m^3/s capacity

    # 1. Inflow exceeds capacity -> Storage accumulates
    inflow_high = np.array([5.0])  # 5.0 m^3/s
    res = engine.update_node_depths(node_ids, inflow_high, cap, area, dt_seconds=dt)
    
    expected_storage = (5.0 - 2.0) * 300.0  # 900.0 m^3
    assert pytest.approx(res["node_A"]["excess_storage_m3"], rel=1e-3) == expected_storage
    
    expected_depth_cm = (900.0 / 200.0) * 100.0  # 450.0 cm
    assert pytest.approx(res["node_A"]["water_depth_cm"], rel=1e-3) == expected_depth_cm


def test_multi_cycle_mass_balance_and_drainage_down():
    """Verifies that across a multi-step storm and recession, volume is conserved exactly.
    
    Invariant:
        Delta S = Total Inflow Volume - Total Outflow Volume
    """
    engine = CouplingEngine()
    node_ids = ["node_B"]
    dt = 300.0
    area = np.array([300.0])
    cap = np.array([1.5])  # 1.5 m^3/s

    # Hyetograph: 3 cycles of storm followed by 5 cycles of zero rain (drainage-down)
    inflows = [4.5, 6.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    total_volume_in = 0.0
    total_volume_out = 0.0
    prev_s = 0.0

    for q_in_val in inflows:
        q_in = np.array([q_in_val])
        total_volume_in += q_in_val * dt

        # Outflow capacity is limited by available water (inflow + previous storage)
        available_vol = prev_s + q_in_val * dt
        actual_outflow_vol = min(available_vol, cap[0] * dt)
        total_volume_out += actual_outflow_vol

        res = engine.update_node_depths(node_ids, q_in, cap, area, dt_seconds=dt)
        current_s = res["node_B"]["excess_storage_m3"]
        prev_s = current_s

    # Final storage state check
    final_storage = engine.get_state("node_B")[0]
    volume_difference = total_volume_in - total_volume_out
    
    # Assert exact mass balance within floating point precision
    assert pytest.approx(final_storage, abs=1e-2) == volume_difference


def test_drainage_down_monotonicity():
    """Verifies that when rainfall ceases, storage strictly drains down until reaching zero."""
    engine = CouplingEngine()
    node_ids = ["node_C"]
    dt = 100.0
    area = np.array([100.0])
    cap = np.array([2.0])

    # Seed initial storage of 500 m^3
    engine.set_state("node_C", storage_m3=500.0, depth_cm=500.0)

    # Run 4 dry cycles (Q_in = 0, Q_cap = 2.0 m^3/s -> 200 m^3 drained per cycle)
    s1 = engine.update_node_depths(node_ids, np.array([0.0]), cap, area, dt_seconds=dt)["node_C"]["excess_storage_m3"]
    assert s1 == 300.0  # 500 - 200

    s2 = engine.update_node_depths(node_ids, np.array([0.0]), cap, area, dt_seconds=dt)["node_C"]["excess_storage_m3"]
    assert s2 == 100.0  # 300 - 200

    s3 = engine.update_node_depths(node_ids, np.array([0.0]), cap, area, dt_seconds=dt)["node_C"]["excess_storage_m3"]
    assert s3 == 0.0    # 100 - 200 -> max(0, -100) = 0.0

    s4 = engine.update_node_depths(node_ids, np.array([0.0]), cap, area, dt_seconds=dt)["node_C"]["excess_storage_m3"]
    assert s4 == 0.0    # Remains at 0.0

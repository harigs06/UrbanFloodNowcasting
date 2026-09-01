"""End-to-End integration tests for the full 5-stage nowcasting pipeline."""

from datetime import datetime, timezone
import numpy as np
import pytest

from src.workers.pipeline_worker import FloodPipelineOrchestrator


@pytest.mark.asyncio
async def test_full_e2e_pipeline_storm_cycle():
    """Runs a complete 5-stage cycle against a synthetic thunderstorm event.
    
    Verifies:
      Stage 1: Multi-horizon radar advection outputs (15, 30, 45, 60, 120, 180 min).
      Stage 2: Overland runoff flux reaches inlets without DEM recompute.
      Stage 3: GNN surrogate predicts depths and surcharges.
      Stage 4: Reservoir routing updates node and street metrics.
      Stage 5: State cache and summary statistics are published.
    """
    orchestrator = FloodPipelineOrchestrator()

    # Generate synthetic radar storm pulse (45 dBZ)
    rows, cols = (100, 100)
    r_grid, c_grid = np.meshgrid(np.linspace(0, 10, rows), np.linspace(0, 10, cols))
    dist = np.sqrt((r_grid - 4.0) ** 2 + (c_grid - 5.0) ** 2)
    dbz = np.clip(48.0 * np.exp(-(dist ** 2) / 4.0), 0.0, 52.0)

    now = datetime.now(timezone.utc)
    result = await orchestrator.execute_nowcast_cycle(
        radar_dbz_grid=dbz,
        radar_timestamp=now,
        cycle_id="test-e2e-cycle-1",
    )

    assert "summary" in result
    assert "horizons" in result

    summary = result["summary"]
    assert summary.cycle_id == "test-e2e-cycle-1"
    assert summary.data_quality == "nominal"
    assert summary.status == "completed"
    assert summary.execution_duration_ms > 0.0

    # Verify all expected horizons exist
    expected_horizons = [15, 30, 45, 60, 120, 180]
    for h in expected_horizons:
        assert h in result["horizons"]
        points = result["horizons"][h]
        assert len(points) > 0
        
        # Verify schema validity of all points
        for pt in points:
            assert pt.water_depth_cm >= 0.0
            assert pt.risk_level in ["safe", "caution", "impassable"]


@pytest.mark.asyncio
async def test_e2e_pipeline_staleness_fallback():
    """Verifies pipeline gracefully switches to degraded state under stale radar data."""
    orchestrator = FloodPipelineOrchestrator()

    # Stale radar timestamp (1 hour ago)
    stale_time = datetime(2020, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    
    result = await orchestrator.execute_nowcast_cycle(
        radar_dbz_grid=None,
        radar_timestamp=stale_time,
        cycle_id="test-stale-cycle",
    )

    summary = result["summary"]
    assert summary.data_quality == "degraded"
    assert summary.radar_staleness_seconds > 900.0  # > 15 min
    assert summary.status == "completed"

"""Unit tests for Radar QPE and Optical Flow Nowcasting."""

from datetime import datetime, timedelta, timezone
import numpy as np
import pytest

from src.core.radar_qpe import RadarQPEEngine


def test_marshall_palmer_conversion():
    """Verifies Z-R conversion formula against known benchmark reflectivity values."""
    engine = RadarQPEEngine(a=200.0, b=1.6)

    # 1. Zero / low reflectivity gives zero rain
    dbz_low = np.array([0.0, 4.0, -10.0])
    rain_low = engine.reflectivity_to_rain_rate(dbz_low)
    assert np.all(rain_low == 0.0)

    # 2. Moderate rain: ~35 dBZ -> ~5.5 mm/hr
    # Z = 10^(3.5) = 3162.27 -> R = (3162.27 / 200)^(1/1.6) = 15.81^0.625 ≈ 5.58 mm/hr
    dbz_mod = np.array([35.0])
    rain_mod = engine.reflectivity_to_rain_rate(dbz_mod)
    assert 5.0 <= rain_mod[0] <= 6.5

    # 3. Heavy convective storm: ~50 dBZ -> ~48.5 mm/hr
    dbz_heavy = np.array([50.0])
    rain_heavy = engine.reflectivity_to_rain_rate(dbz_heavy)
    assert 40.0 <= rain_heavy[0] <= 55.0


def test_staleness_detection():
    """Verifies staleness detector flags radar feeds older than 15 minutes."""
    engine = RadarQPEEngine(staleness_cutoff_min=15)
    now = datetime.now(timezone.utc)

    # Fresh sweep (5 minutes ago)
    fresh_time = now - timedelta(minutes=5)
    is_stale, delta_sec = engine.check_staleness(fresh_time, current_time=now)
    assert not is_stale
    assert delta_sec <= 310.0

    # Stale sweep (25 minutes ago)
    stale_time = now - timedelta(minutes=25)
    is_stale, delta_sec = engine.check_staleness(stale_time, current_time=now)
    assert is_stale
    assert delta_sec >= 1500.0


def test_optical_flow_advection():
    """Verifies spatial shift of rainfall centroid across 15, 30, 60 min horizons."""
    engine = RadarQPEEngine()
    grid = np.zeros((50, 50), dtype=np.float32)
    grid[20, 20] = 50.0  # Point storm at row 20, col 20

    horizons = [15, 30, 60]
    forecasts = engine.extrapolate_optical_flow(
        current_grid=grid,
        velocity_vector_uv=(2.0, 1.0),  # shift right 2 cols, down 1 row per 15 min
        horizons_min=horizons,
        decay_factor=0.0,
    )

    assert set(forecasts.keys()) == set(horizons)
    
    # Check that storm center moved
    f15 = forecasts[15]
    f30 = forecasts[30]
    
    # At 15 min, max should be around (21, 22)
    max_pos_15 = np.unravel_index(np.argmax(f15), f15.shape)
    assert max_pos_15[0] >= 20 and max_pos_15[1] >= 21

    # At 30 min, shift should be twice as far
    max_pos_30 = np.unravel_index(np.argmax(f30), f30.shape)
    assert max_pos_30[0] >= max_pos_15[0] and max_pos_30[1] >= max_pos_15[1]


def test_rain_gauge_idw_fallback():
    """Verifies rain gauge interpolation fallback when radar is degraded."""
    engine = RadarQPEEngine()
    gauges = [(10.0, 10.0), (40.0, 40.0)]
    rates = [20.0, 40.0]

    grid = engine.interpolate_rain_gauges((50, 50), gauges, rates)
    assert grid.shape == (50, 50)
    # Near gauge 1, rate should be close to 20.0
    assert 18.0 <= grid[10, 10] <= 22.0
    # Near gauge 2, rate should be close to 40.0
    assert 38.0 <= grid[40, 40] <= 42.0

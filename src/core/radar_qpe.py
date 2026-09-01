"""Radar Quantitative Precipitation Estimation (QPE) and Optical Flow Nowcasting.

Features:
1. Marshall-Palmer Z-R conversion: Z = a * R^b (Z in mm^6/m^3 -> R in mm/hr).
2. Optical-flow advection nowcasting across horizons: 15, 30, 45, 60, 120, 180 min.
3. Staleness detector: flags 'degraded' quality if radar sweep is older than 15 min
   and switches to rain-gauge spatial interpolation fallback.
"""

from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple
import numpy as np
from scipy.ndimage import shift

from src.config import settings


class RadarQPEEngine:
    """Processes Doppler radar sweeps and produces multi-horizon rainfall forecasts."""

    def __init__(
        self,
        a: float = settings.MARSHALL_PALMER_A,
        b: float = settings.MARSHALL_PALMER_B,
        staleness_cutoff_min: int = settings.RADAR_STALENESS_THRESHOLD_MINUTES,
    ):
        self.a = a
        self.b = b
        self.staleness_cutoff_min = staleness_cutoff_min

    def reflectivity_to_rain_rate(self, dbz: np.ndarray) -> np.ndarray:
        """Converts Radar Reflectivity Factor (dBZ) to Rainfall Rate (mm/hr).
        
        Formula:
            Z = 10^(dBZ / 10)
            R = (Z / a)^(1 / b)
        """
        # Mask noise below 5 dBZ (non-precipitating / clutter)
        clean_dbz = np.where(dbz < 5.0, -np.inf, dbz)
        z = np.power(10.0, clean_dbz / 10.0)
        z = np.nan_to_num(z, nan=0.0, posinf=0.0, neginf=0.0)

        # Invert Marshall-Palmer Z-R relation
        rain_rate_mm_hr = np.power(np.maximum(0.0, z / self.a), 1.0 / self.b)
        return rain_rate_mm_hr.astype(np.float32)

    def check_staleness(
        self,
        radar_timestamp: Optional[datetime],
        current_time: Optional[datetime] = None,
    ) -> Tuple[bool, float]:
        """Checks whether the latest radar sweep exceeds the staleness threshold.
        
        Returns:
            is_stale (bool), staleness_seconds (float)
        """
        if radar_timestamp is None:
            return True, float("inf")

        now = current_time or datetime.now(timezone.utc)
        if radar_timestamp.tzinfo is None:
            radar_timestamp = radar_timestamp.replace(tzinfo=timezone.utc)
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)

        delta = (now - radar_timestamp).total_seconds()
        is_stale = delta > (self.staleness_cutoff_min * 60.0)
        return is_stale, max(0.0, delta)

    def extrapolate_optical_flow(
        self,
        current_grid: np.ndarray,
        velocity_vector_uv: Tuple[float, float],
        horizons_min: List[int] = settings.NOWCAST_HORIZONS_MINUTES,
        decay_factor: float = 0.002,  # Slight storm intensity decay over time
    ) -> Dict[int, np.ndarray]:
        """Extrapolates radar rainfall grid across future horizons via optical flow advection.
        
        Args:
            current_grid: 2D array of current rain rate (mm/hr).
            velocity_vector_uv: (u, v) storm motion vector in grid cells per 15 min.
            horizons_min: forecast lead times in minutes.
            decay_factor: rate of convective dissipation.
            
        Returns:
            Dictionary mapping horizon_minutes -> 2D forecast rain rate grid.
        """
        forecasts = {}
        u, v = velocity_vector_uv

        for horizon in horizons_min:
            # Scale displacement based on horizon duration
            steps = horizon / 15.0
            shift_r = v * steps
            shift_c = u * steps

            # Apply semi-Lagrangian spatial shift
            shifted = shift(current_grid, shift=(shift_r, shift_c), mode='constant', cval=0.0)
            
            # Apply temporal decay for long horizons
            temporal_decay = np.exp(-decay_factor * horizon)
            advected_grid = np.clip(shifted * temporal_decay, 0.0, None).astype(np.float32)
            
            forecasts[horizon] = advected_grid

        return forecasts

    def interpolate_rain_gauges(
        self,
        grid_shape: Tuple[int, int],
        gauge_locations: List[Tuple[float, float]],
        gauge_rates: List[float],
    ) -> np.ndarray:
        """Inverse Distance Weighted (IDW) interpolation fallback when radar feed is degraded."""
        rows, cols = grid_shape
        if not gauge_locations or not gauge_rates:
            # Return baseline uniform drizzle if no gauges provided
            return np.full((rows, cols), 5.0, dtype=np.float32)

        r_grid, c_grid = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')
        weights_sum = np.zeros((rows, cols), dtype=np.float64)
        weighted_val = np.zeros((rows, cols), dtype=np.float64)

        for (gr, gc), rate in zip(gauge_locations, gauge_rates):
            dist = np.sqrt((r_grid - gr) ** 2 + (c_grid - gc) ** 2) + 1e-3
            w = 1.0 / (dist ** 2)
            weights_sum += w
            weighted_val += w * rate

        rain_grid = (weighted_val / weights_sum).astype(np.float32)
        return rain_grid

    def process_nowcast_cycle(
        self,
        radar_dbz_grid: Optional[np.ndarray],
        radar_timestamp: Optional[datetime],
        velocity_vector_uv: Tuple[float, float] = (1.5, -0.8),
        grid_shape: Tuple[int, int] = (100, 100),
        gauge_locations: Optional[List[Tuple[float, float]]] = None,
        gauge_rates: Optional[List[float]] = None,
        current_time: Optional[datetime] = None,
    ) -> Tuple[Dict[int, np.ndarray], str, float]:
        """Main entry point for radar ingestion and nowcasting.
        
        Returns:
            (forecasts_by_horizon, data_quality, staleness_seconds)
        """
        is_stale, staleness_sec = self.check_staleness(radar_timestamp, current_time)

        if is_stale or radar_dbz_grid is None:
            # Fallback to rain gauge IDW interpolation
            data_quality = "degraded"
            base_rain_rate = self.interpolate_rain_gauges(
                grid_shape=grid_shape,
                gauge_locations=gauge_locations or [(20, 30), (70, 80), (50, 50)],
                gauge_rates=gauge_rates or [15.0, 35.0, 22.0],
            )
        else:
            data_quality = "nominal"
            base_rain_rate = self.reflectivity_to_rain_rate(radar_dbz_grid)

        # Generate multi-horizon forecasts
        forecasts = self.extrapolate_optical_flow(
            current_grid=base_rain_rate,
            velocity_vector_uv=velocity_vector_uv,
        )

        return forecasts, data_quality, staleness_sec

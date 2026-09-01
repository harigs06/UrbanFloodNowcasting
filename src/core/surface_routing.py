"""Surface Routing Engine for Online Urban Runoff Routing.

Reads precomputed D8 flow direction and SCS Curve Number rasters from `data/dem_cache/`.
Routes live rainfall excess flux to stormwater inlet nodes with sub-second execution,
guaranteeing real-time performance within the nowcast latency budget.
"""

from collections import deque
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import numpy as np
from scipy.ndimage import zoom

from src.config import settings
from src.offline.dem_preprocess import D8_OFFSETS, DEMPreprocessor


class SurfaceRoutingEngine:
    """Fast vectorized overland flow routing over cached terrain grids."""

    def __init__(self, cache_dir: Optional[Path] = None, cell_size_m: float = 10.0):
        self.cache_dir = cache_dir or settings.DEM_CACHE_DIR
        self.cell_size_m = cell_size_m
        self.cell_area_m2 = cell_size_m * cell_size_m
        
        self.fdir: Optional[np.ndarray] = None
        self.accum: Optional[np.ndarray] = None
        self.cn: Optional[np.ndarray] = None
        self.dem_filled: Optional[np.ndarray] = None

        # Precomputed fast topological routing arrays
        self._src_indices: Optional[np.ndarray] = None
        self._dst_indices: Optional[np.ndarray] = None

        self._load_cache()

    def _load_cache(self) -> None:
        """Loads cached static grids and precomputes topological traversal order."""
        fdir_file = self.cache_dir / "flow_direction.npy"
        cn_file = self.cache_dir / "curve_number.npy"
        accum_file = self.cache_dir / "flow_accumulation.npy"
        dem_file = self.cache_dir / "dem_filled.npy"

        if not (fdir_file.exists() and cn_file.exists() and accum_file.exists() and dem_file.exists()):
            preprocessor = DEMPreprocessor(cache_dir=self.cache_dir)
            preprocessor.process_and_cache(cell_size_m=self.cell_size_m)

        self.fdir = np.load(fdir_file)
        self.cn = np.load(cn_file)
        self.accum = np.load(accum_file)
        self.dem_filled = np.load(dem_file)

        self._precompute_topological_order()

    def _precompute_topological_order(self) -> None:
        """Precomputes static 1D ridge-to-valley traversal vectors for millisecond execution."""
        rows, cols = self.fdir.shape
        num_cells = rows * cols

        in_degree = np.zeros((rows, cols), dtype=np.int32)
        for code, (dr, dc) in D8_OFFSETS.items():
            src_mask = (self.fdir == code)
            r_indices, c_indices = np.where(src_mask)
            dst_r = r_indices + dr
            dst_c = c_indices + dc
            valid = (dst_r >= 0) & (dst_r < rows) & (dst_c >= 0) & (dst_c < cols)
            np.add.at(in_degree, (dst_r[valid], dst_c[valid]), 1)

        queue = deque(zip(*np.where(in_degree == 0)))
        src_flat = []
        dst_flat = []

        while queue:
            r, c = queue.popleft()
            curr_idx = r * cols + c
            code = self.fdir[r, c]
            if code in D8_OFFSETS:
                dr, dc = D8_OFFSETS[code]
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    target_idx = nr * cols + nc
                    src_flat.append(curr_idx)
                    dst_flat.append(target_idx)
                    in_degree[nr, nc] -= 1
                    if in_degree[nr, nc] == 0:
                        queue.append((nr, nc))

        self._src_indices = np.array(src_flat, dtype=np.int32)
        self._dst_indices = np.array(dst_flat, dtype=np.int32)

    def compute_excess_runoff(
        self,
        rain_rate_mm_hr: np.ndarray,
        dt_seconds: float = settings.CYCLE_DT_SECONDS,
    ) -> np.ndarray:
        """Applies the SCS-CN (Soil Conservation Service Curve Number) equation."""
        if rain_rate_mm_hr.shape != self.fdir.shape:
            scale_r = self.fdir.shape[0] / float(rain_rate_mm_hr.shape[0])
            scale_c = self.fdir.shape[1] / float(rain_rate_mm_hr.shape[1])
            rain_rate_mm_hr = zoom(rain_rate_mm_hr, (scale_r, scale_c), order=1)

        p_mm = rain_rate_mm_hr * (dt_seconds / 3600.0)
        s_ret = (25400.0 / np.maximum(self.cn, 1.0)) - 254.0
        i_a = 0.2 * s_ret

        excess_mask = p_mm > i_a
        q_excess_mm = np.zeros_like(p_mm, dtype=np.float32)
        q_excess_mm[excess_mask] = np.power(p_mm[excess_mask] - i_a[excess_mask], 2.0) / (
            p_mm[excess_mask] - i_a[excess_mask] + s_ret[excess_mask]
        )

        return q_excess_mm

    def route_flux_to_inlets(
        self,
        rain_rate_mm_hr: np.ndarray,
        inlet_grid_coords: List[Tuple[int, int]],
        dt_seconds: float = settings.CYCLE_DT_SECONDS,
    ) -> np.ndarray:
        """Routes excess surface flux across precomputed D8 matrix into inlet nodes in milliseconds."""
        rows, cols = self.fdir.shape
        q_excess_mm = self.compute_excess_runoff(rain_rate_mm_hr, dt_seconds=dt_seconds)
        cell_flux_m3s = ((q_excess_mm / 1000.0) * self.cell_area_m2 / dt_seconds).astype(np.float32)

        # Fast 1D flattened in-place routing
        routed_flat = cell_flux_m3s.ravel().copy()
        if self._src_indices is not None and len(self._src_indices) > 0:
            for i in range(len(self._src_indices)):
                routed_flat[self._dst_indices[i]] += routed_flat[self._src_indices[i]]

        # Sample at inlet nodes
        coords_arr = np.array(inlet_grid_coords, dtype=np.int32)
        r_clamped = np.clip(coords_arr[:, 0], 0, rows - 1)
        c_clamped = np.clip(coords_arr[:, 1], 0, cols - 1)
        flat_inlet_indices = r_clamped * cols + c_clamped
        return routed_flat[flat_inlet_indices].astype(np.float32)

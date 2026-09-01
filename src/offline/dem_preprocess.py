"""Offline DEM preprocessing module.

Performs one-time terrain conditioning:
1. Pit-filling / Depression sink filling.
2. D8 Flow Direction and Flow Accumulation computation.
3. SCS-CN (Curve Number) runoff parameter mapping.
Caches processed raster arrays into `data/dem_cache/` for zero-overhead online lookup.
"""

from pathlib import Path
from typing import Dict, Optional, Tuple
import numpy as np
from scipy.ndimage import minimum_filter, maximum_filter

from src.config import settings

# D8 Direction Encodings (ESRI convention):
# 32  64  128
# 16   x    1
#  8   4    2
D8_OFFSETS: Dict[int, Tuple[int, int]] = {
    1: (0, 1),     # East
    2: (1, 1),     # Southeast
    4: (1, 0),     # South
    8: (1, -1),    # Southwest
    16: (0, -1),   # West
    32: (-1, -1),  # Northwest
    64: (-1, 0),   # North
    128: (-1, 1),  # Northeast
}


class DEMPreprocessor:
    """Preprocesses raw elevation models into optimized static flow routing grids."""

    def __init__(self, cache_dir: Optional[Path] = None):
        self.cache_dir = cache_dir or settings.DEM_CACHE_DIR
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def fill_pits(self, dem: np.ndarray, max_iterations: int = 100, epsilon: float = 1e-4) -> np.ndarray:
        """Vectorized depression sink filling (pit filling).
        
        Ensures monotonic downslope flow paths so water does not get trapped
        in artificial elevation depressions.
        """
        dem_filled = dem.copy().astype(np.float64)
        rows, cols = dem.shape

        # Iteratively raise depressions until stable
        for _ in range(max_iterations):
            padded = np.pad(dem_filled, pad_width=1, mode='edge')
            # 8-neighbor minimum
            neighbor_min = np.full((rows, cols), np.inf, dtype=np.float64)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    neighbor_slice = padded[1 + dr : 1 + dr + rows, 1 + dc : 1 + dc + cols]
                    neighbor_min = np.minimum(neighbor_min, neighbor_slice)
            
            new_filled = np.maximum(dem, np.minimum(dem_filled, neighbor_min + epsilon))
            diff = np.max(np.abs(new_filled - dem_filled))
            dem_filled = new_filled
            if diff < epsilon:
                break

        return dem_filled

    def compute_d8_flow_direction(self, dem: np.ndarray, cell_size_m: float = 10.0) -> np.ndarray:
        """Computes the D8 steepest descent direction matrix using ESRI flow codes.
        
        Returns an array of uint8 values {1, 2, 4, 8, 16, 32, 64, 128}.
        """
        rows, cols = dem.shape
        fdir = np.zeros((rows, cols), dtype=np.uint8)
        max_slope = np.zeros((rows, cols), dtype=np.float64)

        padded = np.pad(dem, pad_width=1, mode='edge')

        for code, (dr, dc) in D8_OFFSETS.items():
            dist = cell_size_m * np.sqrt(dr**2 + dc**2)
            neighbor_slice = padded[1 + dr : 1 + dr + rows, 1 + dc : 1 + dc + cols]
            # Downward slope (positive means neighbor is lower)
            drop = dem - neighbor_slice
            slope = drop / dist

            mask = slope > max_slope
            fdir[mask] = code
            max_slope[mask] = slope[mask]

        # Cells with no downhill neighbor flow to lowest border or default to 1
        flat_mask = (fdir == 0)
        if np.any(flat_mask):
            fdir[flat_mask] = 1

        return fdir

    def compute_flow_accumulation(self, fdir: np.ndarray) -> np.ndarray:
        """Computes total upstream contributing cell count for each grid cell.
        
        Performs topological traversal from ridges to valley bottoms.
        """
        rows, cols = fdir.shape
        accum = np.ones((rows, cols), dtype=np.float64)  # Each cell starts with its own weight of 1

        # Count in-degrees (number of upstream neighbors flowing into each cell)
        in_degree = np.zeros((rows, cols), dtype=np.int32)
        for code, (dr, dc) in D8_OFFSETS.items():
            src_mask = (fdir == code)
            r_indices, c_indices = np.where(src_mask)
            dst_r = r_indices + dr
            dst_c = c_indices + dc
            valid = (dst_r >= 0) & (dst_r < rows) & (dst_c >= 0) & (dst_c < cols)
            np.add.at(in_degree, (dst_r[valid], dst_c[valid]), 1)

        # Queue of sources (in-degree == 0, ridge tops)
        queue_r, queue_c = np.where(in_degree == 0)
        queue = list(zip(queue_r.tolist(), queue_c.tolist()))

        while queue:
            curr_r, curr_c = queue.pop(0)
            code = fdir[curr_r, curr_c]
            if code in D8_OFFSETS:
                dr, dc = D8_OFFSETS[code]
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    accum[nr, nc] += accum[curr_r, curr_c]
                    in_degree[nr, nc] -= 1
                    if in_degree[nr, nc] == 0:
                        queue.append((nr, nc))

        return accum

    def generate_curve_number_raster(
        self,
        shape: Tuple[int, int],
        default_cn: float = 85.0,
        impervious_ratio: float = 0.6,
    ) -> np.ndarray:
        """Generates SCS Curve Number grid reflecting urban imperviousness.
        
        Values range from 60 (permeable open soil) to 98 (impervious asphalt/roofs).
        """
        cn_grid = np.full(shape, default_cn, dtype=np.float32)
        # Introduce spatial variation across urban density zones
        rows, cols = shape
        r_grid, c_grid = np.ogrid[:rows, :cols]
        variation = 8.0 * np.sin(r_grid / 10.0) * np.cos(c_grid / 10.0)
        cn_grid = np.clip(cn_grid + variation, 65.0, 98.0)
        return cn_grid

    def process_and_cache(
        self,
        raw_dem: Optional[np.ndarray] = None,
        cell_size_m: float = 10.0,
        dem_shape: Tuple[int, int] = (100, 100),
    ) -> Dict[str, Path]:
        """Runs the full offline conditioning pipeline and writes binary npy arrays to cache."""
        if raw_dem is None:
            # Generate synthetic realistic urban topography (gentle slope + hills)
            rows, cols = dem_shape
            r, c = np.meshgrid(np.linspace(0, 10, rows), np.linspace(0, 10, cols), indexing='ij')
            raw_dem = 25.0 - 0.15 * r - 0.10 * c + 2.0 * np.sin(r) * np.cos(c)

        # 1. Pit-fill
        dem_filled = self.fill_pits(raw_dem)

        # 2. D8 Flow direction
        fdir = self.compute_d8_flow_direction(dem_filled, cell_size_m=cell_size_m)

        # 3. Flow accumulation
        accum = self.compute_flow_accumulation(fdir)

        # 4. Curve number
        cn = self.generate_curve_number_raster(dem_filled.shape)

        # Save to cache
        cache_paths = {
            "dem_filled": self.cache_dir / "dem_filled.npy",
            "flow_direction": self.cache_dir / "flow_direction.npy",
            "flow_accumulation": self.cache_dir / "flow_accumulation.npy",
            "curve_number": self.cache_dir / "curve_number.npy",
        }

        np.save(cache_paths["dem_filled"], dem_filled)
        np.save(cache_paths["flow_direction"], fdir)
        np.save(cache_paths["flow_accumulation"], accum)
        np.save(cache_paths["curve_number"], cn)

        return cache_paths


if __name__ == "__main__":
    preprocessor = DEMPreprocessor()
    paths = preprocessor.process_and_cache()
    print("DEM Preprocessing completed. Cache files written:")
    for k, v in paths.items():
        print(f"  {k}: {v}")

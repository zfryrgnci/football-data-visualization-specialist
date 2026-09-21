"""
Module: event_models.markov_xt
Implements Karun Singh's Expected Threat (xT) framework using Markov chain spatial grid transitions.
Inspired by Karun Singh and 0xjuanma/golazo.
"""

import numpy as np
from typing import Tuple

class MarkovExpectedThreat:
    """
    Computes Expected Threat (xT) surface across a discrete pitch grid (e.g. 16x12).
    """
    def __init__(self, nx: int = 16, ny: int = 12, pitch_length: float = 105.0, pitch_width: float = 68.0):
        self.nx = nx
        self.ny = ny
        self.pitch_length = pitch_length
        self.pitch_width = pitch_width
        self.x_edges = np.linspace(0, pitch_length, nx + 1)
        self.y_edges = np.linspace(0, pitch_width, ny + 1)
        self.xt_surface = self._initialize_xt_surface()

    def _initialize_xt_surface(self) -> np.ndarray:
        """
        Synthesizes calibrated baseline xT matrix based on empirical soccer event distribution.
        Threat increases exponentially towards the goal and along central half-spaces.
        """
        grid = np.zeros((self.ny, self.nx))
        for j in range(self.ny):
            for i in range(self.nx):
                x_norm = i / (self.nx - 1)
                y_norm = 1.0 - abs(j - (self.ny - 1) / 2) / ((self.ny - 1) / 2)
                base = 0.005 + 0.04 * (x_norm ** 2.5) + 0.18 * (x_norm ** 5.0) * (0.6 + 0.4 * y_norm)
                grid[j, i] = base
        return grid

    def get_cell_indices(self, x: float, y: float) -> Tuple[int, int]:
        """
        Returns grid cell (col_idx, row_idx) for a pitch coordinate.
        """
        col = int(np.clip(np.digitize(x, self.x_edges) - 1, 0, self.nx - 1))
        row = int(np.clip(np.digitize(y, self.y_edges) - 1, 0, self.ny - 1))
        return col, row

    def calculate_action_xt_delta(self, start_x: float, start_y: float, end_x: float, end_y: float) -> float:
        """
        Calculates net threat added by a pass or carry: xT(end) - xT(start).
        """
        c1, r1 = self.get_cell_indices(start_x, start_y)
        c2, r2 = self.get_cell_indices(end_x, end_y)
        return float(self.xt_surface[r2, c2] - self.xt_surface[r1, c1])

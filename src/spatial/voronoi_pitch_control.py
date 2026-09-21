"""
Module: spatial.voronoi_pitch_control
Computes Voronoi spatial pitch dominance and team tactical convex hulls.
Inspired by eddwebster/football_analytics.
"""

import numpy as np
from scipy.spatial import Voronoi, ConvexHull
from typing import Dict, Tuple, List

class PitchControlAnalyzer:
    """
    Analyzes spatial dominance, territorial ownership, and tactical team shape.
    """
    def __init__(self, pitch_length: float = 105.0, pitch_width: float = 68.0):
        self.length = pitch_length
        self.width = pitch_width

    def compute_team_convex_hull(self, player_coords: np.ndarray) -> Dict[str, float]:
        """
        Computes the convex hull bounding the outfield players.
        Returns:
            area (m^2), width (m), depth (m), and centroid (X, Y).
        """
        if len(player_coords) < 3:
            return {"area": 0.0, "width": 0.0, "depth": 0.0, "centroid_x": 0.0, "centroid_y": 0.0}
        
        hull = ConvexHull(player_coords)
        width = float(np.max(player_coords[:, 1]) - np.min(player_coords[:, 1]))
        depth = float(np.max(player_coords[:, 0]) - np.min(player_coords[:, 0]))
        centroid = np.mean(player_coords, axis=0)
        
        return {
            "area": float(hull.volume), # in 2D, volume is area
            "width": width,
            "depth": depth,
            "centroid_x": float(centroid[0]),
            "centroid_y": float(centroid[1]),
            "vertices": player_coords[hull.vertices].tolist()
        }

    def compute_voronoi_tessellation(self, home_pts: np.ndarray, away_pts: np.ndarray) -> Voronoi:
        """
        Constructs Voronoi diagram bounded by pitch dimensions.
        """
        # Add perimeter boundary anchors to enforce clipping
        boundary = np.array([
            [-20, -20], [self.length + 20, -20],
            [self.length + 20, self.width + 20], [-20, self.width + 20],
            [self.length / 2, -30], [self.length / 2, self.width + 30]
        ])
        all_points = np.vstack([home_pts, away_pts, boundary])
        return Voronoi(all_points)

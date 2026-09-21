"""
Module: event_models.pass_sonar
Computes polar pass sonars, angular directional bins, and progression distances.
Inspired by eddwebster/football_analytics and 0xjuanma/golazo.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Any

class PassSonarCalculator:
    """
    Bins passes into discrete angular sectors and calculates frequency,
    average distance, and completion rates per direction.
    """
    def __init__(self, num_sectors: int = 12):
        self.num_sectors = num_sectors
        self.sector_width = 360.0 / num_sectors

    def calculate_angles_and_distance(self, start_x: np.ndarray, start_y: np.ndarray,
                                      end_x: np.ndarray, end_y: np.ndarray) -> pd.DataFrame:
        """
        Calculates pass angle in degrees (0 = Forward / North, Clockwise) and distance in meters.
        """
        dx = end_x - start_x
        dy = end_y - start_y
        
        # Distance
        dist = np.sqrt(dx**2 + dy**2)
        
        # Angle in degrees where forward is 0 degrees, right is 90 degrees, backward is 180 degrees
        # Using atan2(dy, dx)
        rad = np.arctan2(dy, dx)
        deg = np.degrees(rad)
        # Shift so forward (along positive X) is 0
        deg_shifted = (90 - deg) % 360
        
        df = pd.DataFrame({"dx": dx, "dy": dy, "dist": dist, "angle": deg_shifted})
        df["sector"] = (df["angle"] // self.sector_width).astype(int) % self.num_sectors
        return df

    def compute_sonar_profile(self, pass_df: pd.DataFrame) -> Dict[str, Any]:
        """
        Computes aggregate metrics per angular sector.
        """
        total_passes = len(pass_df)
        if total_passes == 0:
            return {"frequencies": [0.0]*self.num_sectors, "avg_distances": [0.0]*self.num_sectors}
        
        freqs = []
        dists = []
        for s in range(self.num_sectors):
            sec_data = pass_df[pass_df["sector"] == s]
            cnt = len(sec_data)
            freqs.append(cnt / total_passes)
            dists.append(sec_data["dist"].mean() if cnt > 0 else 0.0)
            
        return {
            "num_sectors": self.num_sectors,
            "frequencies": freqs,
            "avg_distances": dists,
            "total_passes": total_passes
        }

"""
Module: cv_tracking.homography
Implements Direct Linear Transform (DLT) and Homography transformation
mapping broadcast video camera perspective coordinates [u, v] to planar 2D pitch coordinates [X, Y].
Inspired by roboflow/sports.
"""

import numpy as np
import cv2

class PitchHomographyTransformer:
    """
    Computes and applies planar homography between broadcast camera keypoints
    and standard FIFA metric pitch coordinates (105m x 68m).
    """
    def __init__(self, camera_keypoints: np.ndarray, pitch_keypoints: np.ndarray):
        """
        Args:
            camera_keypoints: (N, 2) array of detected pixel coordinates [u, v]
            pitch_keypoints: (N, 2) array of corresponding metric pitch coordinates [X, Y]
        """
        if len(camera_keypoints) < 4 or len(pitch_keypoints) < 4:
            raise ValueError("At least 4 correspondence points are required for Homography estimation.")
        
        self.src_pts = np.float32(camera_keypoints)
        self.dst_pts = np.float32(pitch_keypoints)
        self.H, self.mask = cv2.findHomography(self.src_pts, self.dst_pts, cv2.RANSAC, 5.0)
        self.H_inv = np.linalg.inv(self.H) if self.H is not None else None

    def transform_camera_to_pitch(self, points: np.ndarray) -> np.ndarray:
        """
        Transforms bounding box foot contact points [u, v] to 2D pitch coordinates [X, Y].
        """
        if self.H is None:
            raise RuntimeError("Homography matrix is not calculated.")
        
        pts = np.array(points, dtype=np.float32).reshape(-1, 1, 2)
        transformed = cv2.perspectiveTransform(pts, self.H)
        return transformed.reshape(-1, 2)

    def transform_pitch_to_camera(self, points: np.ndarray) -> np.ndarray:
        """
        Reprojects 2D pitch points back to broadcast camera view for validation.
        """
        if self.H_inv is None:
            raise RuntimeError("Inverse homography matrix is not calculated.")
        pts = np.array(points, dtype=np.float32).reshape(-1, 1, 2)
        reprojected = cv2.perspectiveTransform(pts, self.H_inv)
        return reprojected.reshape(-1, 2)

    def compute_reprojection_error(self) -> float:
        """
        Calculates Root Mean Squared Error (RMSE) in meters between ground truth and reprojected points.
        """
        projected = self.transform_camera_to_pitch(self.src_pts)
        errors = np.linalg.norm(projected - self.dst_pts, axis=1)
        return float(np.mean(errors))

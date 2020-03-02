import cv2
import numpy as np


def solve_pnp(object_2d):
    object_3d_points = np.array(([0, 180, 0],
                                [0, 0, 0],
                                [217, 0, 0],
                                [217, 180, 0]), dtype=np.double)
    object_2d_point = np.array(object_2d, dtype=np.double)
    camera_matrix = np.array(([5000, 0, 2008.0],
                             [0, 5000, 952.0],
                             [0, 0, 1.0]), dtype=np.double)
    dist_coefs = np.array([-0.189314, 0.444657, -0.00116176, 0.00164877, -2.57547], dtype=np.double)
    # 求解相机位姿
    found, rvec, tvec = cv2.solvePnP(object_3d_points, object_2d_point, camera_matrix, dist_coefs)
    rotM = cv2.Rodrigues(rvec)[0]
    camera_postion = -np.matrix(rotM).T * np.matrix(tvec)
    print(camera_postion.T)
    return camera_postion.T

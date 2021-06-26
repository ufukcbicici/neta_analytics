import os
import shutil
import numpy as np
from itertools import chain, combinations
from pathmanager import PathManager

PATH_MANAGER = PathManager()


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def affine_transform_points_2d(transform_matrix, points):
        assert transform_matrix.shape[0] == transform_matrix.shape[1] == 3
        assert len(points.shape) == 2 and points.shape[1] == 2
        points_homogenous = np.concatenate([points, np.ones_like(points[:, 0])[:, np.newaxis]], axis=1)
        points_transformed = (transform_matrix @ points_homogenous.T).T
        points_transformed = points_transformed[:, 0:2]
        return points_transformed

    @staticmethod
    def create_directory(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.mkdir(path)

    @staticmethod
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

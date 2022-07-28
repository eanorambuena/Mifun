import numpy as np
import math

class Camera3d:

    def __init__(self, alpha, beta, near, far):
        self.alpha = alpha
        self.beta = beta
        self.near = near
        self.far = far

        self.delta = self.far - self.near
        self.T = self.calculate_transform_matrix()

    def calculate_transform_matrix(self):
        A = (self.far + self.near) / self.delta
        B = 2 * self.near * self.far / self.delta

        return np.array(
            [
                [math.tan(self.alpha), 0, 0, 0],
                [0, math.tan(self.beta), 0, 0],
                [0, 0, A, B],
                [0, 0, -1, 0]
            ]
        )

    def calculate_position(self, r):
        x = r[0]
        y = r[1]
        z = r[2]
        R = np.array([x, y, z, 1])
        position = R.dot(self.T)
        transformed_x = position[0]
        transformed_y = position[1]
        return [int(transformed_x), int(transformed_y)]

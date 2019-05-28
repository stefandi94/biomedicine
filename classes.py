import numpy as np
import matplotlib.pyplot as plt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def toString(self):
        print('(x, y) = ({}, {})'.format(self.x, self.y))


class Bone:

    def __init__(self, points):
        n = len(points)
        self.matrix = np.zeros((n, 2))

        for i, point in enumerate(points):
            self.matrix[i] = np.array([point.getX(), point.getY()])

    def update_points(self, matrix):
        self.matrix = matrix

    def to_vector(self):
        m, n = self.matrix.shape
        row_vector = np.reshape(self.matrix, m*n)
        return row_vector

    def plot(self):
        plt.plot(self.matrix[:, 0], self.matrix[:, 1])

    def toString(self):
        for row in self.matrix:
            print('(x, y) = ({}, {})'.format(row[0], row[1]))

class Joint:

    def __init__(self, upper_bone, lower_bone):
        self.upper_bone = upper_bone
        self.lower_bone = lower_bone

    def update_bones(self, new_upper_bone, new_lower_bone):
        self.upper_bone.update_points(new_upper_bone)
        self.lower_bone.update_points(new_lower_bone)

    def plot(self):
        self.upper_bone.plot()
        self.lower_bone.plot()

    def toString(self):
        print('Upper bone:')
        self.upper_bone.toString()
        print('Lower bone:')
        self.lower_bone.toString()
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
        self.n = len(points)
        self.matrix = np.zeros((self.n, 2))

        for i, point in enumerate(points):
            self.matrix[i] = np.array([point.getX(), point.getY()])

    def get_data(self):
        return self.matrix

    def shape(self):
        return self.n, 2

    def update(self, matrix):
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
        n = upper_bone.shape()[0]
        m = lower_bone.shape()[0]

        self.skip_link = n # this is ad hoc solution to problem with plotting
        self.data = np.zeros((n + m, 2))

        counter = 0
        for row in upper_bone.get_data():
            self.data[counter] = row
            counter += 1

        for row in lower_bone.get_data():
            self.data[counter] = row
            counter += 1

    def update(self, joint):
        self.data = joint

    def to_vector(self):
        m, n = self.data.shape
        row_vector = np.reshape(self.data, m*n)
        return row_vector

    def plot(self):
        plt.plot(self.data[:self.skip_link, 0], self.data[:self.skip_link, 1])
        plt.plot(self.data[self.skip_link+1:, 0], self.data[self.skip_link+1:, 1])

    def toString(self):
        for row in self.data:
            print('(x, y) = ({}, {})'.format(row[0], row[1]))
import matplotlib.pyplot as plt
import numpy as np
import os

from sklearn.decomposition import PCA

from io_functions import read_file
from scipy.spatial import procrustes


def rigidly_align_joints(joints):
    for joint in joints:
        _, joint_centered, _ = procrustes(joints[0].data, joint.data)

        # reduce number of decimal points
        joint_centered = np.around(joint_centered, decimals=3)

        joint.update(joint_centered)


def sample_matrix(joints):
    m = len(joints)
    n = joints[0].data.size
    sample_matrix = np.zeros((m, n))

    for i, joint in enumerate(joints):
        sample_matrix[i] = joint.to_vector()

    return sample_matrix


def plot_shapes_in_dir(path):
    for file in os.listdir(path):
        # plt.figure()
        joint = read_file(os.path.join(path, file))
        joint.plot()
        # plt.title(file)
        # plt.savefig(os.path.join(PLOT_DIR, file.split('.')[0]))


def plot_shapes(list_of_joints):
    plt.figure()
    for joint in list_of_joints:
        joint.plot()

def pca_transform(data, n_components=2):
    pca = PCA(n_components=n_components)
    pca_matrix = pca.fit_transform(data)
    return pca_matrix

def manual_n_components():
    all_ok = False
    while not all_ok:
        print("Enter number of components for PCA")
        n_components = input()
        try:
            n_components = int(n_components)
            if n_components > 0:
                all_ok = True
            else:
                print("Number must be greater than 0")
                continue
        except:
            print("Input must be integer value and greater than 0")
            continue
    return n_components

def solve_for_b(joint, mean_shape,  pca_matrix):
    '''
    System looks like Z = M + Pb
    where Z is a shape, M is mean shape, P is matrix obtained after PCA transformation
    and b is a vector that is used to derive new shape, i.e tweaking values of b will
    give new shapes
    '''
    U, S, V = np.linalg.svd(pca_matrix, full_matrices=False)
    temp = U.transpose() @ (joint.to_vector() - mean_shape)
    b = V @ temp
    return b


def find_b(joints, mean_shape, pca_matrix):
    '''
    Solves linear system Z = M + Pb for b for each joint and returns value of b for each given joint
    '''
    bs = []
    for joint in joints:
        b = solve_for_b(joint, mean_shape, pca_matrix)
        bs.append(b)
    return bs


def get_new_shape(mean, std, mean_shape, pca_matrix):
    b = np.random.normal(mean, std**2)
    new_sample_vector = mean_shape + np.dot(pca_matrix, b)
    new_sample = np.reshape(new_sample_vector, (-1, 2))
    return new_sample

def get_mean(data):
    mean = np.mean(data, axis=0)
    return mean

def get_std(data):
    std = np.std(data, axis=0)
    return std

def plot(sample, skip_link):
    fig = plt.figure()
    a = fig.add_subplot(111)
    a.plot(sample[:skip_link, 0], sample[:skip_link, 1])
    a.plot(sample[skip_link+1:, 0], sample[skip_link+1:, 1])
    return fig


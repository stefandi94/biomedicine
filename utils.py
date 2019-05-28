import matplotlib.pyplot as plt
import numpy as np
import os
from io_functions import read_file
from scipy.spatial import procrustes


def rigidly_align_joints(joints):
    for joint in joints:
        _, upper_bone_centered, _ = procrustes(joints[0].upper_bone.matrix, joint.upper_bone.matrix)
        _, lower_bone_centered, _ = procrustes(joints[0].lower_bone.matrix, joint.lower_bone.matrix)

        upper_bone_centered = np.around(upper_bone_centered, decimals=3)
        lower_bone_centered = np.around(lower_bone_centered, decimals=3)

        joint.update_bones(upper_bone_centered, lower_bone_centered)


def sample_covariance_matrices(joints):
    m = len(joints)
    n1 = joints[0].upper_bone.matrix.size
    n2 = joints[0].lower_bone.matrix.size
    upper_bone_vector = np.zeros((m, n1))
    lower_bone_vector = np.zeros((m, n2))

    for i, joint in enumerate(joints):
        upper_bone_vector[i] = joint.upper_bone.to_vector()
        lower_bone_vector[i] = joint.lower_bone.to_vector()

    upper_bone_mean = np.mean(upper_bone_vector, axis=0)
    lower_bone_mean = np.mean(lower_bone_vector, axis=0)

    upper_bone_vector = upper_bone_vector - upper_bone_mean
    lower_bone_vector = lower_bone_vector - lower_bone_mean

    sample_covariance_matrix_upper = np.cov(upper_bone_vector.T)
    sample_covariance_matrix_lower = np.cov(lower_bone_vector.T)

    return sample_covariance_matrix_upper, sample_covariance_matrix_lower


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
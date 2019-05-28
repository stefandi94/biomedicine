import numpy as np
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.utils.extmath import randomized_svd


from io_functions import find_landmarks_and_write_them_to_a_file, read_files, read_file
from settings import POINTS_DIR, IMAGE_DIR, PLOT_DIR
from utils import rigidly_align_joints, plot_shapes, sample_covariance_matrices
import matplotlib.pyplot as plt

find_landmarks_and_write_them_to_a_file(IMAGE_DIR)

joints = read_files(POINTS_DIR)

plot_shapes(joints)

rigidly_align_joints(joints)

plot_shapes(joints)

sample_covariance_matrix_upper, sample_covariance_matrix_lower = sample_covariance_matrices(joints)

plt.show()

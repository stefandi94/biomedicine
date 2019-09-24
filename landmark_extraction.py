import numpy as np

from io_functions import find_landmarks_and_write_them_to_a_file, read_files
from utils import rigidly_align_joints, plot_shapes, sample_matrix, find_b, \
    get_mean, get_std, pca_transform, plot, get_new_shape, manual_n_components
from GUI import GUI

from settings import POINTS_DIR, IMAGE_DIR

import random
random.seed(5)

# find_landmarks_and_write_them_to_a_file(IMAGE_DIR)

joints = read_files(POINTS_DIR)
skip_link = joints[0].skip_link
# plot_shapes(joints)

rigidly_align_joints(joints)

# plot_shapes(joints)

sample_matrix = sample_matrix(joints)
mean_sample_matrix = np.mean(sample_matrix, axis=0)

n_components = manual_n_components()
# n_components = 5
pca_matrix = pca_transform(sample_matrix.T, n_components)

list_of_b = find_b(joints, mean_sample_matrix, pca_matrix)

mean = get_mean(list_of_b)
std = get_std(list_of_b)

new_sample = get_new_shape(mean, std, mean_sample_matrix, pca_matrix)

GUI(n_components, new_sample, skip_link, mean, std, mean_sample_matrix, pca_matrix)


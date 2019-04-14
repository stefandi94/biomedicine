import numpy as np
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.utils.extmath import randomized_svd


from io_functions import find_landmarks_and_write_them_to_a_file, pts_to_vectors
from settings import POINTS_DIR, IMAGE_DIR

x = find_landmarks_and_write_them_to_a_file(IMAGE_DIR)

# mean_black = np.zeros((22, 2))
# mean_white = np.zeros((18, 2))
#
#
# pts_vectors = pts_to_vectors(POINTS_DIR)
print()
# for pts_file in pts_vectors.values():
#     mean_black += pts_file[0]
#     mean_white += pts_file[1]
#
# mean_white /= len(pts_vectors)
# mean_black /= len(pts_vectors)
#
# list_of_black_matrices = []
# list_of_white_matrices = []
#
# for pts_vector in pts_vectors.keys():
#     list_of_black_matrices.append(pts_vectors[pts_vector][0] - mean_black)
#     list_of_white_matrices.append(pts_vectors[pts_vector][1] - mean_white)
#
# black = np.vstack(list_of_black_matrices)
# white = np.vstack(list_of_white_matrices)
#
# black_cov = np.cov(black)
# white_cov = np.cov(white)
#
#
# Ub, sb, Vb = randomized_svd(black_cov,
#                               n_components=black_cov.shape[0]-1,
#                               n_iter=5,
#                               random_state=None)
#
# Uw, sw, Vw = randomized_svd(white_cov,
#                               n_components=white_cov.shape[0]-1,
#                               n_iter=5,
#                               random_state=None)
#
#
# pca = PCA(n_components=1)
#
# black_dim_red = pca.fit_transform(black_cov)
# white_dim_red = pca.fit_transform(white_cov)
#
#
#
# import manpo
#
# print()

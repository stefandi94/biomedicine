from pathlib import Path
import menpo.io as mio
from menpo.visualize import print_progress
from settings import POINTS_DIR, IMAGE_DIR
from io_functions import pts_to_vectors

pts_points = pts_to_vectors(IMAGE_DIR)
path_to_lfpw = POINTS_DIR
training_shapes = []

for lg in print_progress(mio.import_landmark_files(path_to_lfpw / '*.pts', verbose=True)):
    training_shapes.append(lg)
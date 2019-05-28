import os
from io_functions import file_read


def plot_shapes(path):
    for file in os.listdir(path):
        # plt.figure()
        joint = file_read(os.path.join(path, file))
        joint.plot()
        # plt.title(file)
        # plt.savefig(os.path.join(PLOT_DIR, file.split('.')[0]))
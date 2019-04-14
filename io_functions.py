import glob
import os
import os.path as osp
import numpy as np
from PIL import Image

from settings import IMAGE_DIR, POINTS_DIR


def find_landmarks_and_write_them_to_a_file(path):
    """Takes pictures with marked landmarks and creates a subdirectory containing .pts files with coordinate of
    those landmarks
    Format of created files:

    Numbers of point: <number of points>
    {
    ...
    xi yi
    ...
    }
    \n
    \n

    ...
    xi yi
    ...
    }
    """

    image_names = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.png'):
           image_names.append(file)
    # image_names = glob.glob('*.png')

    if not osp.exists(POINTS_DIR):
        os.makedirs(POINTS_DIR)


    for image in image_names:
        
        # separate path into filepath and extension
        filename, file_extension = os.path.splitext(image)

        im = Image.open(osp.join(IMAGE_DIR, image))
        w, h = im.size

        black_coor = []
        white_coor = []

        for i in range(h):
            for j in range(w):
                v = im.getpixel((j, i))
                if 0 == v[0]:
                    black_coor.append(j)
                    black_coor.append(i)
                if 255 == v[0]:
                    white_coor.append(j)
                    white_coor.append(i)

        write_points_in_file(filename, black_coor + white_coor)


def write_points_from_multiple_list_in_file(filename, lst):
    myfile = open(filename, 'w')

    for i, l in enumerate(lst):
        if 0 == i:
            write_points_in_file(myfile, l)
        else:
            write_points_in_file(myfile, l, True)

    myfile.close()


def write_points_in_file(filename, list_of_points):
    """
    Writes list of point pair-wise to the file
    if add_space_between, 2 blank lines will be added
    :param filename:
    :param list_of_points:
    :return:
    """

    myfile = open(osp.join(POINTS_DIR, filename + '.pts'), 'w')
    columns = ('a ' *len(list_of_points)).split()
    for col in columns:
        myfile.write("{} ".format(col))
    myfile.write("\n")

    for point in list_of_points:
        myfile.write("{0} ".format(point))


def pts_to_vectors(path):
    """Takes path to directory where .pts files are and returns dictionary where filename is a key and value is list
    of nx2 matrices where first matrix represents coordinates of upper (black) joint and second of lower (white) joint"""

    points_files = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.pts'):
            points_files.append(file)

    dt = {}

    for filename in points_files:
        with open(osp.join(POINTS_DIR, filename), 'r') as file:
            points = file.readline().split("")
        dt[filename] = points

    return dt
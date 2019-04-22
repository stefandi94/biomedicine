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

        red_coor = []
        green_coor = []

        for i in range(h):
            for j in range(w):
                v = im.getpixel((j, i))
                if v[0]/(sum(v[:3])+1) > 0.9:
                    red_coor.append(j)
                    red_coor.append(i)
                if v[1]/(sum(v[:3])+1) > 0.9:
                    green_coor.append(j)
                    green_coor.append(i)

        if len(red_coor) != 18 or len(green_coor) != 20:
            print('Filename: {}' .format(filename))
            print('\tNumber of red points: {}' .format(len(red_coor)))
            print('\tNumber of green points: {}' .format(len(green_coor)))
            print('\n')

        myfile = open(osp.join(POINTS_DIR, filename + '.pts'), 'w')
        write_points_from_multiple_list_in_file(myfile, [red_coor, green_coor])


def write_points_from_multiple_list_in_file(myfile, lst):
    # myfile = open(filename, 'w')

    for i, l in enumerate(lst):
        if 0 == i:
            write_points_in_file(myfile, l)
        else:
            write_points_in_file(myfile, l, True)

    myfile.close()


def write_points_in_file(myfile, list_of_points, add_space_between=False):
    """
    Writes list of point pair-wise to the file
    if add_space_between, 2 blank lines will be added
    :param filename:
    :param list_of_points:
    :return:
    """


    if add_space_between:
        myfile.write('\n\n')


    num_of_points = int(len(list_of_points) / 2)
    myfile.write('Number of points: {0}'.format(num_of_points))
    myfile.write('\n{')
    for i in range(len(list_of_points)):
        if 0 == i % 2:
            myfile.write('\n')
        myfile.write("{0}".format(list_of_points[i]))
        if i != len(list_of_points) - 1:
            myfile.write(' ')
        else:
            myfile.write('\n}')


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
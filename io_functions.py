import glob
import os
import numpy as np
from PIL import Image


def find_landmarks_and_write_them_to_a_file(path):
    '''Takes pictures with marked landmarks and creates a subdirectory containing .pts files with coordinate of
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
    }'''

    os.chdir(path)
    imgs = glob.glob('*.png')

    for el in imgs:

        tokens = el.split('.')
        im = Image.open(el)
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

        write_points_from_multiple_list_in_file('../points/' + tokens[0] + '.pts', [black_coor, white_coor])


def write_points_from_multiple_list_in_file(filename, lst):
    myfile = open(filename, 'w')
    n = len(lst)

    for i, l in enumerate(lst):
        if 0 == i:
            write_points_in_file(myfile, l)
        else:
            write_points_in_file(myfile, l, True)

    myfile.close()


def write_points_in_file(myfile, lst, add_space_between=False):
    ''' writes list of point pair-wise to the file
    if add_space_between, 2 blank lines will be added'''
    if add_space_between:
        myfile.write('\n\n')

    num_of_points = int(len(lst)/2)
    myfile.write('Number of points: {0}'.format(num_of_points))
    myfile.write('\n{')
    for i in range(len(lst)):
        if 0 == i%2:
            myfile.write('\n')
        myfile.write("{0}".format(lst[i]))
        if i != len(lst)-1:
            myfile.write(' ')
        else:
            myfile.write('\n}')


def pts_to_vectors(path):
    '''Takes path to directoru where .pts files are and returns dictionary where filename is a key and value is list
    of nx2 matices where first matrix represents coordinates of upper (black) joint and second of lower (white) joint'''

    os.chdir(path)
    points_files = glob.glob('*.pts')
    dt = {}
    for filename in points_files:
        vector_list = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                tokens = line.split(' ')
                if '}' == tokens[0]:
                    vector_list.append(M)
                if 'Number' == tokens[0]:
                    m = int(tokens[3])
                    M = np.zeros((m, 2))
                    i = 0
                elif 3 == len(tokens) or 2 == len(tokens):
                    M[i, 0] = tokens[0]
                    M[i, 1] = tokens[1]
                    i += 1
        dt[filename] = vector_list
    return dt
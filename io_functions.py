import os
import os.path as osp
from PIL import Image
from classes import Point, Bone, Joint
from settings import IMAGE_DIR, POINTS_DIR


def find_landmarks_and_write_them_to_a_file(path):
    """Takes pictures with marked landmarks and creates a subdirectory containing .pts files with coordinate of
    those landmarks
    Format of created files:

    Upper bone
    [
    ...
    xi yi
    ...
    ]
    \n
    Lower bone
    [
    ...
    xi yi
    ...
    ]
    """

    image_names = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.png'):
            image_names.append(file)

    if not osp.exists(POINTS_DIR):
        os.makedirs(POINTS_DIR)

    for image in image_names:
        # separate path into filepath and extension
        filename, file_extension = os.path.splitext(image)
        im = Image.open(osp.join(IMAGE_DIR, image))
        w, h = im.size

        lower_bone = []
        upper_bone = []

        for i in range(h):
            for j in range(w):
                v = im.getpixel((j, i))

                # We made a mistake while marking so not all markers are true green or true red
                # To bypass this problem only pixels that are 90% green or red are taken
                # +1 is added to sum to avoid division by zero. It does not change result so no pixel is misclassified

                if v[0]/(sum(v[:3])+1) > 0.9:
                    lower_bone.append(j)
                    lower_bone.append(i)
                if v[1]/(sum(v[:3])+1) > 0.9:
                    upper_bone.append(j)
                    upper_bone.append(i)

        myfile = open(osp.join(POINTS_DIR, filename + '.pts'), 'w')
        write_points_from_multiple_list_in_file(myfile, [upper_bone, lower_bone])


def write_points_from_multiple_list_in_file(myfile, lst):
    for i, l in enumerate(lst):
        if 0 == i:
            myfile.write('Upper bone')
            write_points_in_file(myfile, l)
        else:
            myfile.write('\n\nLower bone')
            write_points_in_file(myfile, l)

    myfile.close()


def write_points_in_file(myfile, list_of_points):
    """
    Writes list of point pair-wise to the file
    if add_space_between, 2 blank lines will be added
    :param filename:
    :param list_of_points:
    :return:
    """
    myfile.write('\n[')
    for i in range(len(list_of_points)):
        if 0 == i % 2:
            myfile.write('\n')
        myfile.write("{0}".format(list_of_points[i]))
        if i != len(list_of_points) - 1:
            myfile.write(' ')
        else:
            myfile.write('\n]')


def read_file(path):
    with open(path, 'r') as file:
        bones = []
        for line in file.readlines():
            line = line.rstrip()
            tokens = line.split(' ')
            if '[' == tokens[0]:
                list_of_points = []
            elif ']' == tokens[0]:
                bones.append(Bone(list_of_points))
            else:
                try:
                    x = int(tokens[0])
                    y = int(tokens[1])
                    point = Point(x, y)
                    list_of_points.append(point)
                except:
                    pass
        joint = Joint(bones[0], bones[1])
    return joint


def read_files(path):
    points_files = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.pts'):
            points_files.append(file)

    joints = []
    for filename in points_files:
        joint = read_file(osp.join(POINTS_DIR, filename))
        joints.append(joint)

    return joints

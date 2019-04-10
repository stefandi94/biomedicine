from PIL import Image
import glob
import os
from helper_functions import write_points_from_multiple_list_in_file

os.chdir('./landmarks/images')

imgs = glob.glob('*.png')
for el in imgs:

    tokens = el.split('.')
    im = Image.open(el)
    w, h = im.size

    black_coor = []
    white_coor = []

    for i in range(h):
        for j in range(w):
            v, _ = im.getpixel((j, i))
            if 0 == v:
                black_coor.append(j)
                black_coor.append(i)
            if 255 == v:
                white_coor.append(j)
                white_coor.append(i)

    # myfile = open(tokens[0] + '.pts', 'w')
    #
    # write_points_in_file(myfile, black_coor)
    # write_points_in_file(myfile, white_coor, True)
    #
    # myfile.close()
    write_points_from_multiple_list_in_file('../points/' + tokens[0] + '.pts', [black_coor, white_coor])

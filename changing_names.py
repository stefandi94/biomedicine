import os
import re
import shutil

os.chdir('/home/stefan/PycharmProjects/data/hands')

for index, filename in enumerate(os.listdir(os.getcwd())):
    if 'PA' in os.path.splitext("%s" % filename)[0]:
        # save
        name = filename.replace(".", "_").split("_")[:-1]
        new_name = "%i" % index
        for substring in name:

            try:
                num_in_string = number = re.search(r'\d+', substring).group()
                if isinstance(int(num_in_string), int):
                    substring += ""

            except:
                new_name += "_" + substring


        is_left = 'left'in new_name.lower() or 'l' in new_name.lower()
        is_right = 'right' in new_name.lower() or 'r' in new_name.lower()
     #   is_both = 'both' in new_name.lower() or 'b' in new_name.lower()

        if is_left == True:
            shutil.copyfile("%s" % filename,
                        '/home/stefan/PycharmProjects/data/left_hand/%s.png' %new_name)

        elif is_right == True:
            shutil.copyfile("%s" % filename,
                        '/home/stefan/PycharmProjects/data/right_hand/%s.png' %new_name)

        else:
            shutil.copyfile("%s" % filename,
                        '/home/stefan/PycharmProjects/data/both_hands/%s.png' %new_name)

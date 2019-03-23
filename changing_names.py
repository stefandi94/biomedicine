import os
import re
import shutil

os.chdir('/home/stefan/PycharmProjects/data/hands')

for index, filename in enumerate(os.listdir(os.getcwd())):
    # use only images which have PA in name(relevant for our project)
    if 'PA' in os.path.splitext("%s" % filename)[0]:

        # replace all dots with underscore, split by underscore and separate to tokens and extension
        name = filename.replace(".", "_").split("_")
        list_of_tokens = name[:-1]
        extension = name[-1:]

        new_name = "%i" % index
        for token in list_of_tokens:

            try:
                # if number is in token, ignore it, add empty token to new name
                num_in_string = number = re.search(r'\d+', token).group()
                if isinstance(int(num_in_string), int):
                    token += ""

                # else if number is not in token, add token and separate it with underscore
            except:
                new_name += "_" + token

        # check if new name has left or l in it, indicating left hand
        is_left = 'left'in new_name.lower() or 'l' in new_name.lower()

        # check if new name has right or r in it, indicating right hand
        is_right = 'right' in new_name.lower() or 'r' in new_name.lower()

        # check if new name has both or b in it, indicating both hands
     #   is_both = 'both' in new_name.lower() or 'b' in new_name.lower()

        if is_left == True:
            shutil.copyfile("%s" % filename,
                        '/home/stefan/PycharmProjects/data/left_hand/%s.%s' % (new_name, extension))

        elif is_right == True:
            shutil.copyfile("%s" % filename,
                        '/home/stefan/PycharmProjects/data/right_hand/%s.%s' % (new_name, extension))

        else:
            shutil.copyfile("%s" % filename,
                        '/home/stefan/PycharmProjects/data/both_hands/%s.%s' % (new_name, extension))
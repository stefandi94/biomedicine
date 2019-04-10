def write_points_in_file(myfile, lst, add_space_between=False):
    ''' writes list of point pair-wise to the file
    if add_space_between, 2 blank lines will be added'''
    if add_space_between:
        myfile.write('\n\n')

    myfile.write('{')
    for i in range(len(lst)):
        if 0 == i%2:
            myfile.write('\n')
        myfile.write("{0}".format(lst[i]))
        if i != len(lst)-1:
            myfile.write(' ')
        else:
            myfile.write('\n}')

def write_points_from_multiple_list_in_file(filename, lst):
    myfile = open(filename, 'w')
    n = len(lst)

    for i, l in enumerate(lst):
        if 0 == i:
            write_points_in_file(myfile, l)
        else:
            write_points_in_file(myfile, l, True)

    myfile.close()
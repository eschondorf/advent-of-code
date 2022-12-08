import util
import math
import time
import copy
import pprint

def solver(inpt):
    rv1 = 0
    rv2 = 0
    filesize = {}
    subdir = {}
    current_dir = ""
    for i, line in enumerate(inpt):
        line_lst = line.split(" ")
        if line_lst[1] == 'cd' and line_lst[2] != '..':
            if line_lst[2] == '/':
                current_dir = line_lst[2]
            else:
                if current_dir != '/':
                    current_dir = current_dir + "/" + line_lst[2]
                else:
                    current_dir = current_dir + line_lst[2]
            filesize[current_dir] = 0
            subdir[current_dir] = []
        elif line_lst[1] == 'cd' and line_lst[2] == '..':
            current_dir = '/'.join(current_dir.split('/')[:-1])
        elif line_lst[0] == 'dir':
             subdir[current_dir].append(line_lst[1])
        elif line_lst[0].isdigit():
            filesize[current_dir] += int(line_lst[0])

    rec_helper(subdir, filesize, '/')

    for key in filesize.keys():
        if filesize[key] < 100000:
            rv1 += filesize[key]
    
    avaliable_space = 70000000 - filesize['/']
    need_to_remove = 30000000 - avaliable_space

    for key, val in sorted(filesize.items(), key=lambda item: item[1]):
        if val > need_to_remove:
            rv2 = val
            break

    return rv1, rv2


def rec_helper(subdir, filesize, dir):
    if len(subdir[dir]) == 0:
        return filesize[dir]
    else:
        addl_size = 0
        if dir == '/':
            prefix = ""
        else:
            prefix = dir
        for elt in subdir[dir]:
            addl_size += rec_helper(subdir, filesize, prefix + '/' + elt)
        filesize[dir] += addl_size
        return filesize[dir]


if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_7_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_7_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)
    
    
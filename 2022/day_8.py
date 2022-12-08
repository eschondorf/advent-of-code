import util
import math
import time
import copy
import pprint
import numpy as np

def solver(inpt):
    rv1 = 0
    rv2 = 0
    arr = parser(inpt)
    x_max, y_max = arr.shape # get dimensions of grid
    rv1 += (2  * x_max) + (2 * y_max) - 4 # perimeter trees (all visable)
    
    #loop through grid, avoid perimeter trees
    for y, line in enumerate(arr):
        if y!= 0 and y != y_max - 1: # avoid top and bottom but keep indexing
            for x, elt in enumerate(line):
                if x != 0 and x != x_max - 1: # avoid left and right but keep indexing                 
                    right = arr[y, :][x+1:]
                    left = arr[y, :][:x][::-1] #reverse
                    up = arr[:, x][:y][::-1] #reverse
                    down = arr[:, x][y+1:]

                    # Part 1 find all trees that can be seen from at least one edge
                    rv1 += min(np.amax(right), np.amax(left), np.amax(up), np.amax(down)) < elt

                    # Part 2 generate total score for each tree, find max score
                    tmp_score = 1
                    for direction in [right,left, up, down]:
                        dist = 0
                        visible = True
                        for val in direction:
                            if visible:
                                if val < elt:
                                    #The tree next tree is below you, you can see it
                                    dist += 1
                                else:
                                    # Add the last tree you can see (the one blocking you)
                                    # If you hit the edge you do not get this extra tree
                                    dist += 1
                                    visible = False
                        tmp_score *= dist
                    rv2 = max(rv2, tmp_score)
    return rv1, rv2

def parser(inpt):
    arr_lst = []
    for elt in inpt:
        line = []
        for val in elt:
            line.append(int(val))
        arr_lst.append(line)
    return np.array(arr_lst)
    


if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_8_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_8_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)
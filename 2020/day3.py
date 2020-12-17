'''
Day 3
https://adventofcode.com/2020/day/3
'''

import numpy as np
import util


def task_1(arr, right, down):
    '''
    Finds number of trees in infinite repeating grid along slope

    Inputs:
        inpt (lst of str): The grid that is infinitely repeated to the right
        right (int): How many steps right the toboggan takes each step down
        down (int): How nay steps down the toboggan takes each step right

    Returns: num_trees (int): the number of trees encountered
    '''
    num_trees = 0
    col_len = len(arr)
    row_len = len(arr[0])
    i = 0
    step = 0
    while i <= col_len-1:
        if arr[i, (step * right) % row_len] == '#':
            num_trees += 1
        i += down
        step += 1
    return num_trees


def task_2(inpt, tests):
    '''
    Finds the number of trees for a series of paths and gives the multiple

    Input:
        inpt (lst of str): The grid that is infinitely repeated to the right
        tests (lst of tuples): The paths for each test, contains:
            right (int): How many steps right the toboggan takes each step down
            down (int): How nay steps down the toboggan takes each step right
    
    Returns: result (int): number of trees of each of the paths multiplied 
        together
    '''
    result = 1
    for right, down in tests:
        new_trees = task_1(inpt, right, down)
        result *= new_trees
    return result


def convert_to_array(str_lst):
    '''
    Converts list of strings to numpy array

    Inputs:
        str_lst (lst of str): Initial input from text file
    
    Returns: (arr) numpy array corresponding to str_lst
    '''
    lst = []
    for line in str_lst:
         temp_lst = list(line)[:]
         lst.append(temp_lst)
    return np.array(lst)


if __name__ == "__main__":
    tst = util.read_strs('inputs/day3_test_input.txt')
    inpt = util.read_strs('inputs/day3_input.txt')

    tst_arr = convert_to_array(tst)
    arry = convert_to_array(inpt)

    print("TASK 1")
    util.call_and_print(task_1, tst_arr, 3, 1)
    util.call_and_print(task_1, arry, 3, 1)

    print("\nTASK 2")
    tests = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    util.call_and_print(task_2, tst_arr, tests)
    util.call_and_print(task_2, arry, tests)
    
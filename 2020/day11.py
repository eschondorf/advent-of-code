'''
Day 11
https://adventofcode.com/2020/day/12
'''
import util
import numpy as np


def task_solver (inpt, task2):
    '''
    Counts the number of occupied seats after the seating area reaches stability 
        according to task 1 or task 2 rules

    Input:
        - inpt (lst of strs): The initial grid
        - task2 (boolean): A booelan for if using task 2 rules

    Output: an int, the number of occupied seats after stability
    '''
    arr = make_arr(inpt)
    stable = False
    i = 0
    while not stable:
        #print("turn " + str(i))
        #print(arr)
        arr, stable = simulate_one_cycle(arr, task2)
        i += 1
    unique, counts = np.unique(arr, return_counts=True)
    return dict(zip(unique, counts))[1]


def simulate_one_cycle(arr, task2):
    '''
    Simulates one cycle in the seating area

    Input:
        - arr (np.array): the array representing the seating area
        - task2 (boolean): A booelan for if using task 2 rules

    Ouput: 
        - arr (np.array) the updated seating area
        - an boolean for if there have been no changes in the seating area
    '''
    points_to_change = []
    width = len(arr[0,:])
    height = len(arr)
    for y in range(height):
        for x in range(width):
            current_pos = arr[y, x]
            if current_pos != -1:
                if task2:
                    num_occupied = get_num_occupied_task2(arr, y, x, height, width)
                else:
                    num_occupied = get_num_occupied(arr, y, x, height, width)
                if current_pos == 0 and num_occupied == 0:
                    points_to_change.append((y,x))
                elif current_pos == 1:
                    if num_occupied >= 4 and not task2:
                        points_to_change.append((y,x))
                    elif num_occupied >= 5 and task2:
                        points_to_change.append((y, x))
    for y, x in points_to_change:
        arr[y,x] = (arr[y, x] + 1)%2
    return arr, len(points_to_change) == 0

def get_num_occupied(arr, y, x, height, width):
    '''
    Finds the number of occupied seats neighboring a given seat in the seating 
        area
    
    Input:
        - arr (np.array): the array representing the seating area
        - y (int): the y cooridinate of the seat we are finding neighbors for
        - x (int): the x cooridinate of the seat we are finding neighbors for
        - height (int): the height of the seating grid
        - width (int): the width of the seating grid

    Output: int, the number of surronding seats occupied
    '''
    num_occupied = 0
    for i in range(max(0, y-1), min(height, y+2)):
        for j in range(max(0, x-1), min(width, x+2)):
            if (i, j) != (y, x):
                if arr[i, j] == 1:
                    num_occupied += 1
    return num_occupied

def get_num_occupied_task2(arr, y, x, height, width):
    '''
    Finds the number of occupied seats visable from a given seat in the seating 
        area using task 2 rules
    
    Input:
        - arr (np.array): the array representing the seating area
        - y (int): the y cooridinate of the seat we are finding neighbors for
        - x (int): the x cooridinate of the seat we are finding neighbors for
        - height (int): the height of the seating grid
        - width (int): the width of the seating grid

    Output: int, the number of visable seats occupied
    '''
    num_occupied = 0
    for i in range(x+1, width):
        if arr[y, i] == 1:
            num_occupied += 1
            break
        elif arr[y, i] == 0:
            break
    for i in range(1, x+1):
        if arr[y, x-i] == 1:
            num_occupied += 1
            break
        elif arr[y, x-i] == 0:
            break
    for i in range(y+1, height):
        if arr[i, x] == 1:
            num_occupied += 1
            break
        elif arr[i, x] == 0:
            break
    for i in range(1, y+1):
        if arr[y - i, x] == 1:
            num_occupied += 1
            break
        elif arr[y - i, x] == 0:
            break
    for i in range(1, min(width-x, height - y)):
        if arr[y+i, x + i] == 1:
            num_occupied += 1
            break
        elif arr[y+i, x + i] == 0:
            break

    for i in range(1, min(width-x, y+1)):
        if arr[y-i, x + i] == 1:
            num_occupied += 1
            break
        elif arr[y-i, x + i] == 0:
            break

    for i in range(1, min(x+1, height - y)):
        if arr[y+i, x - i] == 1:
            num_occupied += 1
            break
        elif arr[y+i, x - i] == 0:
            break  
    
    for i in range(1, min(x+1, y+1)):
        if arr[y-i, x - i] == 1:
            num_occupied += 1
            break
        elif arr[y-i, x - i] == 0:
            break          
    return num_occupied
        
    


def make_arr(inpt):
    '''
    Makes a np.array from the input

    Input:
        - inpt (lst of strs): the input grid
    
    Output: a np.array representing the input grid
    '''
    dbl_lst = []
    for line in inpt:
        new_line = []
        for elt in line:
            if elt == '.':
                new_line.append(-1)
            elif elt == 'L':
                new_line.append(0)
            elif elt == '#':
                new_line.append(1)
            else:
                print("ERROR")
        dbl_lst.append(new_line)
    return np.array(dbl_lst)

def remake_inpt(arr):
    '''
    Turns np.array back into the input format

    Input:
        - arr (np.array): array representing the seating area grid
    
    Output: a list of strings in the format of the input representing the 
        seating grid
    '''
    rv_lst = []
    for y in range(len(arr)):
        row_str = ''
        for x in range(len(arr[0,:])):
            elt = arr[y, x]
            if elt == 1:
                row_str += '#'
            elif elt == 0:
                row_str += 'L'
            elif elt == -1:
                row_str += '.'
        rv_lst.append(row_str)
    return rv_lst





if __name__ == "__main__":
    tst = util.read_strs('inputs/day11_test.txt', sep = '\n')
    inpt = util.read_strs('inputs/day11_input.txt', sep = '\n')
    
    print('TASK 1')
    util.call_and_print(task_solver, tst, False)
    util.call_and_print(task_solver, inpt, False)

    print('\nTASK2')
    util.call_and_print(task_solver, tst, True)
    util.call_and_print(task_solver, inpt, True)
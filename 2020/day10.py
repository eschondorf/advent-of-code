'''
Day 10
https://adventofcode.com/2020/day/10
Thanks to Borja Sotomayor for help with the task 2 solution. My solution here 
is basically a child of his.
'''
import util


def task1(adapters):
    '''
    Calculates the number of one difference and three difference gaps and 
        returns their product
    
    Input:
        - adapters (lst of ints): the list of adapter voltages

    Outputs: int the multiple of the number and one difference and three 
        difference gaps
    '''
    adapters = sorted(adapters)
    one_diff = 1
    three_diff = 1
    for i, adapt  in enumerate(adapters[:-1]):
        diff = adapters[i+1] - adapt
        if diff == 1:
            one_diff += 1
        elif diff == 3:
            three_diff += 1
    return one_diff * three_diff


def task2(adapters):
    '''
    Calculates the number of valid adapter combinations

    Input:
        - adapters (lst of ints): the list of adapter voltages

    Outputs: int the number of valid adapter combinations
    '''
    adapters = sorted(adapters)
    return generate_valid_lsts(0, adapters, 0, {})


def generate_valid_lsts(start, inpt, i, mem):
    '''
    Recursive helper functions for task 2, calculates the number of valid 
        adapter combinations recursively

    Input:
        - start (int): starting voltage for this round of recursion
        - inpt (lst of strs): the list of adapter voltages
        - i (int): the index of the starting voltage
        - mem (dict): dictionary of past combinations to number of valid 
            sub-lists

    Outputs: arr (int): the number of valid adapter combinations
    '''
    if (i, start) in mem:
        return mem[(i, start)]

    elif i == len(inpt) - 1:
        return 1

    else:
        arr = 0
        for j in range(i, len(inpt)):
            elt = inpt[j]
            if elt - start <= 3:
                arr += generate_valid_lsts(elt, inpt, j+1, mem)
            elif elt - start > 3:
                break
        mem[(i, start)] = arr
    return arr


if __name__ == "__main__":
    tst = util.read_ints('inputs/day10_test.txt')
    tst2 = util.read_ints('inputs/day10_test2.txt')
    inpt = util.read_ints('inputs/day10_input.txt')

    print('TASK 1')
    util.call_and_print(task1, tst)
    util.call_and_print(task1, tst2)
    util.call_and_print(task1, inpt)

    print('\nTASK 2')
    util.call_and_print(task2, tst)
    util.call_and_print(task2, tst2)
    util.call_and_print(task2, inpt)

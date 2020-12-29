'''
Day 9
https://adventofcode.com/2020/day/9
'''
import util


def is_num_valid(preamble, num):
    '''
    Helper function for task 1, checks whether number is valid according to 
        task 1 rules
    
    Input:
        - preamble (lst of ints): list of the preamble elements
        - num (int): the number to be added to

    Output: boolean, if the number is valid according to task 1 rules
    '''
    for i, elt in enumerate(preamble):
        for j, elt_j in enumerate(preamble[i:]):
            if num == elt + elt_j:
                return True
    return False


def task1(inpt, preamble_len):
    '''
    Finds the first number that isn't a sum of two of the prior peramble length 
        number of numbers

    Input:
        - inpt (lst of ints): the input list of numbers
        - preamble_len (int): the lenght of the preamble
    
    Outputs: an int, the first number that isn't a sum of two of the prior 
        peramble length number of numbers
    '''
    for i in range(len(inpt) - preamble_len):
        num = inpt[i + preamble_len]
        preamble = inpt[i: i + preamble_len + 1]
        if not is_num_valid(preamble, num):
            return num

def task2(inpt, num):
    '''
    Finds the sum of a contiguous set maxinum and minimum element of the set of 
        at least two numbers in your list which sum to the invalid number from 
        task 1
    
    Input:
        - inpt (lst of ints): the input list of numbers
        - num (int): the solution to task 1
    
    Output: int, the sum of a contiguous set maxinum and minimum element of the 
        set of at least two numbers in your list which sum to the invalid 
        number from task 1
    '''
    for i,_ in enumerate(inpt):
        sum = 0
        sum_lst = []
        j = 1
        while sum < num:
            sum += inpt[i + j]
            sum_lst.append(inpt[i+j])
            j += 1
            if sum == num:
                return max(sum_lst) + min(sum_lst)




if __name__ == "__main__":
    tst = util.read_ints('inputs/day9_test.txt', sep = '\n')
    inpt = util.read_ints('inputs/day9_input.txt', sep = '\n')

    print('TASK 1')
    util.call_and_print(task1, tst, 5)
    util.call_and_print(task1, inpt, 25)

    print('\nTASK 2')
    util.call_and_print(task2, tst, 127)
    util.call_and_print(task2, inpt, 556543474)


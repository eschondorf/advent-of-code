'''
Day 2
https://adventofcode.com/2020/day/2
'''

import util


def task1(inpt):
    '''
    Counts number of valid passwords (task 1 rules ones with number of 
        characters of ltr between lb and ub) in lst:
    
    Input:
        inpt(lst of strings): lines of inputs broken into strings

    Returns:
        num_valid (int): number of valid passwords
    '''
    num_valid = 0
    for line in inpt:
        lb, ub, ltr, pswrd = read_line(line)
        num_occurences = pswrd.count(ltr)
        if lb <= num_occurences and ub >= num_occurences:
            num_valid += 1
    return num_valid


def task2(inpt):
    '''
    Counts number of valid passwords (task 2 exclusivley either lb or ub 
        contains ltr) in lst:
    
    Input:
        inpt(lst of strings): lines of inputs broken into strings

    Returns:
        num_valid (int): number of valid passwords
    '''
    num_valid = 0
    for line in inpt:
        lb, ub, ltr, pswrd = read_line(line)
        if ((pswrd[lb-1] == ltr and pswrd[ub-1] != ltr) or 
            (pswrd[lb-1] != ltr and pswrd[ub-1] == ltr)):
            num_valid += 1
    return num_valid


def read_line(line):
    '''
    Reads one line of inpt and breaks it into relevent parts.
    
    Inputs:
        line (str): a line of the inpt
    Outputs:
        A tuple (int, int, str, str) containing:
            lb (int): the lower bound/first position
            ub (int): the upper bound/second position
            ltr (str): the letter of interest
            pswrd (str): the password in question
    '''
    line_splt = line.split()
    lb, ub = line_splt[0].split('-')
    ltr = line_splt[1][0]
    pswrd = line_splt[2]
    return (int(lb), int(ub), ltr, pswrd)








if __name__ == "__main__":
    inpt = util.read_strs("inputs/day2_input.txt", sep = '\n')
    tst = util.read_strs("inputs/day2_testinput.txt", sep = '\n')

    print("TASK 1")
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)

    print("\nTASK 2")
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)

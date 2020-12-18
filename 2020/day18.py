'''
Day 18
https://adventofcode.com/2020/day/18

Finished both stars at 01:12 12/18
'''
import util
import math

def task_solver(inpt, task2):
    '''
    Sums the solutions to each line of each experession in the input

    Inputs:
        inpt (lst of str): list of all the expressions
        task2 (boolean): If this expressions should be computed with 
                            task 2 rules
    
    Returns: an integer, the sum of the solutions to each of the expressions
    '''
    sum = 0
    for line in inpt:
        sum += complicated_solver(line, task2)
    return sum


def complicated_solver(line, task2):
    '''
    Solves experssions with parenthesis for either task

    Inputs:
        line (str): An expression in the input
        task2 (boolean): If this expressions should be computed with 
                            task 2 rules
    
    Returns: an integer, the solution to the experssion given the rules 
                defined in the task
    '''
    #base case
    if line.count("(") == 0:
        if task2:
            return simple_solver_task2(str(line))
        else:
            return simple_solver(str(line))

    else: # recursive case, first find the outer-most layer of parenthesis
        first_open = None
        last_open = None
        open_counter = 0
        closed_counter = 0
        for i, elt in enumerate(line):
            if elt == "(":
                open_counter += 1
                if first_open == None:
                    first_open = i
            elif elt == ")":
                closed_counter += 1
                if open_counter == closed_counter:
                    last_open = i
                    break

    val = complicated_solver(line[first_open + 1 : last_open], task2)
    return complicated_solver(line[:first_open] + str(val) 
                                + line[last_open+1:], task2)


def simple_solver(expr):
    '''
    Solves an expersion without parenthesis using task 1 rules

    Input:
        expr (str): The simple expression

    Returns: an integer which is what the expression evaluates to
    '''
    lst = expr.split(" ")
    rv= int(lst[0])
    for item in lst[1:]:
        if item == "+":
            plus = True
            Times = False
            continue
        elif item == "*":
            plus = False
            times = True
            continue
        elif plus:
            rv += int(item)
        elif times:
            rv *= int(item)
    return rv


def simple_solver_task2(expr):
    '''
    Solves an expersion without parenthesis using task 2 rules

    Input:
        expr (str): The simple expression

    Returns: an integer which is what the expression evaluates to
    '''
    lst = expr.split(" ")
    only_mult = add_task2(lst)
    return multiply_list(only_mult)


def add_task2(lst):
    '''
    Takes a simple expression and does all addition in expersion leaving just 
        the multiplication

    Input: lst (lst of chars): the expression broken into a list
    
    Returns: a list with just the numbers that need to be multiplied
    '''
    rv = []
    running_sum = 0
    for i, elt in enumerate(lst):
        if elt != "*" and elt != "+":
            running_sum += int(elt)
        elif elt == "*":
            rv.append(running_sum)
            running_sum = 0
    rv.append(running_sum)
    return rv


def multiply_list(lst) :
    '''
    Simple helper function to multiply elements of a list together. For some 
        reason the one in the math library wasn't working.
    
    Inputs:
        lst (lst): a list of numbers
    
    Returns: result (int/float) the product of all the elements in the list
    '''
    result = 1
    for elt in lst:
         result *=  elt 
    return result 


if __name__ == "__main__":
    smpl_tst = "1 + (2 * 3) + (4 * (5 + 6))"
    smpl_tst2 = "1 + 2 * 3 + 4 * 5 + 6"
    smpl_tst3 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    inpt = util.read_strs("inputs/day18_input.txt", sep = "\n")
    print("TESTING")
    util.call_and_print(complicated_solver, smpl_tst3, True)
    util.call_and_print(simple_solver_task2, smpl_tst2)
    print("\nTASK 1")
    util.call_and_print(task_solver, inpt, False)
    print("\nTASK 2")
    util.call_and_print(task_solver, inpt, True)
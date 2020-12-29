'''
Day 13
https://adventofcode.com/2020/day/13
'''
import util
from sympy.ntheory.modular import crt 

def task1(inpt):
    '''
    Finds shortest waiting time multiplied by that bus id

    Input:
        - inpt (lst of strs): the given input (inital waiting time and bus ids)

    Output: an integer, waiting time * bus id
    '''
    depart_time = int(inpt[0])
    tmp_bus_id = inpt[1].split(',')
    bus_ids = [int(x) for x in tmp_bus_id if x != 'x']
    min_wait = float('inf')
    current_rv = 0
    for bus in bus_ids:
        bus_wait = bus - depart_time % bus
        if bus_wait < min_wait:
            min_wait = bus_wait
            current_rv = bus * bus_wait
    return current_rv


def task2(inpt):
    '''
    Finds first time that satisifies the input string

    Input:
        - inpt (lst of strs): the given input

    Output: an integer representing the first time where the given sequence 
        occurs
    '''
    tmp_bus_id = inpt[1].split(',')
    bus_ids, times = [int(x) for i, x in enumerate(tmp_bus_id) if x != 'x'], [int(x)-i for i, x in enumerate(tmp_bus_id) if x != 'x']
    return crt(bus_ids, times)[0]



if __name__ == "__main__":
    tst = util.read_strs('inputs/day13_test.txt', sep = '\n')
    inpt = util.read_strs('inputs/day13_input.txt', sep = '\n')
    print('TASK 1')
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)
    print('\nTASK 2')
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)
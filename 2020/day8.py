'''
Day 8
https://adventofcode.com/2020/day/8
'''
import util


def task1(lines):
    '''
    Finds the value in the accumulator before an instruction is run a second 
        time
    
    Inputs:
        - lines (lst of strs): the list of commands given

    Outputs: accumulator (int): the value of the accumulator before an 
        instruction is run a second time
    '''
    seen_dict = {}
    accumulator = 0
    i = 0
    last_instruction = 0
    while (not seen_dict.get(i, False) and i < len(lines)):
        line = lines[i]
        seen_dict[i] = True
        j = i
        command, val = line.split(' ')
        if command == 'nop':
            i += 1
        elif command == 'acc':
            accumulator += int(val)
            i += 1
        elif command == 'jmp':
            i += int(val)
    return accumulator


def run_program(commds):
    '''
    Helper function for task 2, runs the program with a list of commands, finds 
        all the 'nop' and 'jmp' commands

    Inputs:
        - commds (lst of strs): the list of commands given

    Outputs:
        - accumulator (int): the value of the accumulator before an 
            instruction is run a second time
        - commds[last_instruction] (str): the last command run
        - last_instruction (int): the index of the last command run
        - to_change (lst of tuples): list of tulples (command (str), 
            index (int)) that may be corupted
    '''
    seen_dict = {}
    accumulator = 0
    i = 0
    last_instruction = 0
    to_change = []
    while (not seen_dict.get(i, False) and i < len(commds)):
        command, val = commds[i]
        seen_dict[i] = True
        last_instruction = i
        if command == 'nop':
            to_change.append((command, i))
            i += 1
        elif command == 'acc':
            accumulator += int(val)
            i += 1
        elif command == 'jmp':
            to_change.append((command, i))
            i += int(val)
    return accumulator, commds[last_instruction], last_instruction, to_change


def task2 (lines):
    '''
    Finds the command that is corrupted and needs to be changed

    Input:
        - lines (lst of strs): the list of commands given

    Outputs:
        - acc (int): the value of the accumulator when the corrupted command is 
            changed and the program run all the way to the end
    '''
    commds = []
    for line in lines:
        command, val = line.split(' ')
        commds.append([command, int(val)])
    n = len(commds)
    acc, last_instruction, j, to_change = run_program(commds)
    for com, i in to_change:
        if com == 'nop':
            to_change_back = 'nop'
            commds[i][0] = 'jmp'
        elif com == 'jmp':
            to_change_back = 'jmp'
            commds[i][0] = 'nop'
        else:
            print("ERROR")
        acc, _, j, _ = run_program(commds)
        if j == n-1:
            return acc
        else:
            commds[i][0] = to_change_back

    
if __name__ == "__main__":
    tst = util.read_strs('inputs/day8_test.txt', sep = '\n')
    inpt = util.read_strs('inputs/day8_input.txt', sep = '\n')

    print('TASK 1')
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)

    print('\nTASK 2')
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)

import util
import math
import time
import copy

def solver(inpt, stack):
    rv1 = ""
    rv2 = ""
    stack2 = copy.deepcopy(stack)
    for line in inpt:
        _, num_to_move, _, frm,  _, to = line.split(" ")
        num_to_move = int(num_to_move)
        for i in range(num_to_move):
            val = stack[frm].pop()
            stack[to].append(val)
        move = stack2[frm][-num_to_move:]
        stack2[frm] = stack2[frm][:-num_to_move]
        stack2[to] = stack2[to] + move 

    for i in range(1, len(stack)+1):
        rv1+= stack[str(i)].pop()
        rv2 += stack2[str(i)].pop()

    return str(rv1), str(rv2)



if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_5_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_5_test.txt", sep = "\n")
    tst = tst[5:]
    tst_dict = {}
    tst_dict['1']  = ['Z', 'N']
    tst_dict['2']  = ['M', 'C', 'D']
    tst_dict['3']  = ['P']
    inpt_dict = {}
    inpt_dict['1']  = ['Z','J','N','W','P','S']
    inpt_dict['2']  = ['G', 'S', 'T']
    inpt_dict['3']  = ['V', 'Q', 'R', 'L', 'H']
    inpt_dict['4']  = ['V', 'S', 'T', 'D']
    inpt_dict['5']  = ['Q','Z','T','D','B','M', 'J']
    inpt_dict['6']  = ['M','W','T','J','D','C', 'Z', 'L']
    inpt_dict['7']  = ['L','P','M','W','G','T', 'J']
    inpt_dict['8']  = ['N','G','M','T','B','F', 'Q', 'H']
    inpt_dict['9']  = ['R','D','G','C','P','B', 'Q', 'W']
    print("TASK 1 and 2")
    util.call_and_print(solver, inpt, inpt_dict)
    util.call_and_print(solver, tst, tst_dict)

    
import util
import math
import time

def solver(inpt):
    rv1 = 0
    rv2 = 0
    tmp = 0
    sup = 0
    for i, num in enumerate(inpt):
        if num is not '':
            tmp += int(num)
        else:
            sup = max(sup, tmp)
            tmp = 0
    
    sup_lst = []
    tmp2 = 0
    for i, num in enumerate(inpt):
        if num is not '':
            tmp2 += int(num)
        else:
            if len(sup_lst) < 3:
                sup_lst.append(tmp2)
                sup_lst.sort()
            else:
                if tmp2 > sup_lst[0]:
                    sup_lst[0] = tmp2
                    sup_lst.sort()
            tmp2 = 0
    rv1 = sup
    rv2 = sum( sup_lst)
    return rv1, rv2





if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_1_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_1_test.txt", sep = "\n")
    print(tst)
    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)


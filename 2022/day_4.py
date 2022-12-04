import util
import math
import time

def solver(inpt):
    rv1 = 0
    rv2 = 0
    for line in inpt:
        ran1, ran2 = line.split(',')
        bin1 = trans_to_binary(ran1)
        bin2 = trans_to_binary(ran2)
        result = bin1 & bin2
        if result == bin1 or result == bin2:
            rv1 += 1
        if result != 0:
            rv2 += 1

    return rv1, rv2

def trans_to_binary(inpt):
    lb = int(inpt.split('-')[0])
    ub = int(inpt.split('-')[1])
    rv = 0
    for i in range(lb, ub+1):
        rv += 2**i

    return rv





if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_4_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_4_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)

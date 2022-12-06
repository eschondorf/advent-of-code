import util
import math
import time
import copy


def solver(inpt, n):
    rv = 0
    inpt = inpt[0]
    for i in range(len(inpt)):
        tmp = set(inpt[i: i+n])
        if len(tmp) == n:
            rv = i+n
            break

    return rv



if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_6_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_6_test.txt", sep = "\n")

    print("TASK 1 and 2")
    print("Test")
    util.call_and_print(solver, tst, 4)
    util.call_and_print(solver, tst, 14)
    print("Solution")
    util.call_and_print(solver, inpt, 4)
    util.call_and_print(solver, inpt, 14)
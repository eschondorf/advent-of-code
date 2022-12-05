import util
import math
import time

def solver(inpt):
    rv1 = 0
    rv2 = 0
    for line in inpt:
        elf, me = line.split(" ")
        elfint = ord(elf) - ord('A') + 1
        meint = ord(me) - ord('W')
        rv1+= meint
        result = (meint - elfint)%3
        rv1 += (3*result + 3)%9

    for line in inpt:
        elf, result = line.split(" ")
        elfint = ord(elf) - ord('A') + 1
        result = (ord(result) - ord('X'))*3
        rv2 +=  result
        rv2 += (elfint - 1 + [2, 0, 1][result/3]) % 3 + 1

    return rv1, rv2





if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_2_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_2_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)


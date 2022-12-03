import util
import math
import time

def solver(inpt):
    rv1 = 0
    rv2 = 0
    for line in inpt:
        first, second = line[:len(line)/2], line[len(line)/2: ]
        first = set(first)
        second = set(second)
        common_letter = first.intersection(second)
        if len(common_letter)!= 1:
            print("ERROR")
        rv1 += priority(common_letter.pop())

    for i in range(0, len(inpt), 3):
        first = set(inpt[i])
        second = set(inpt[i+1])
        third = set(inpt[i+2])
        common_letter = first.intersection(second.intersection(third))
        if len(common_letter)!= 1:
            print("ERROR")
        rv2 += priority(common_letter.pop())


    return rv1, rv2

def priority(char):
    char = str(char)
    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1





if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_3_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_3_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)

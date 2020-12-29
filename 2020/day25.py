'''
Day 25
https://adventofcode.com/2020/day/25
'''
import util

def task1(card, door):
    '''
    Finds the encription key

    Input:
        - card (int): the given card public key
        - door (int): the given door public key

    Outputs: an int, the encryption key
    '''
    val = 1
    i = 0
    while val != card:
        val = one_loop(val, 7)
        i += 1
    card_loop = i
    val = 1
    j = 0
    while val != door:
        val = one_loop(val, 7)
        j += 1
    door_loop = j
    val = 1
    for i in range(card_loop):
        val = one_loop(val, door)
    return val
        


def one_loop(val, subject):
    '''
    Does one loop of transformation

    Inputs:
        val (int): the current value
        subject (int): the subject number to multiply by

    Outputs: an int, the new value
    '''
    val = val * subject
    return val % 20201227




if __name__ == "__main__":
    tst = util.read_strs('inputs/day25_test.txt')
    inpt = util.read_strs('inputs/day25_input.txt')
    tst_card, tst_door = int(tst[0]), int(tst[1])
    inpt_card, inpt_door = int(inpt[0]), int(inpt[1])
    
    print('TASK 1')
    util.call_and_print(task1, tst_card, tst_door)
    util.call_and_print(task1, inpt_card, inpt_door)
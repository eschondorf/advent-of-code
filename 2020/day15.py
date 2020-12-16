'''
Day 15
'''
import time


def tasks(inpt, one_or_two):
    if one_or_two == 1:
        end = 2020
    else:
        end = 30000000
    n = len(inpt)
    d = {}
    current_num = None
    past_num = inpt[-1]
    gap = None
    last_in_lst = inpt[-1] in inpt[:-1]
    for i in range(n-1):
        d[inpt[i]] = i+1
    for i in range(n-1, end-1):
        current_num = d.get(past_num, 0)
        if current_num != 0:
            current_num = i + 1 - current_num
        d[past_num] = i + 1
        past_num = current_num
    return past_num



if __name__ == "__main__":
    inpt = [2,1,10,11,0,6]
    tst = [0,3,6]
    
    print("TASK 1")
    
    util.call_and_print(task1, tst)
    start = time.time()
    util.call_and_print(task1, inpt)
    end = time.time()
    print(end-start)
    '''
    print("TASK 2")
    call_and_print(task2, tst)
    call_and_print(task2, inpt)
    '''
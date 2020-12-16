'''
Day 14
'''
import util
import math

def generate_number(mask, num):
    num_str = bin(int(num))
    mask_str = mask
    length = len(num_str)
    num_str = ((38 - length) * '0') + num_str[2:]
    rv = []
    for i, digit in enumerate(mask_str):
        if digit == 'X':
            if num_str[i] is None:
                rv.append(0)
            else:
                rv.append(int(num_str[i]))
        else:
            rv.append(int(digit))
    ret = int(bin(int(''.join(map(str, rv)), 2) << 1), 2) >> 1
    return ret

def list_combo(lst):
    rv = []
    if len(lst) == 0 or lst == None:
        return []
    else:
        current_val = 2 ** lst[0]
        remaining_lst = list_combo(lst[1:])
        rv = remaining_lst[:]
        rv.append(current_val)
        for elt in remaining_lst:
            rv.append(elt + current_val)
        return rv


def generate_number_task2(mask, num):
    num_str = bin(int(num))
    mask_str = mask
    length = len(num_str)
    X_indicies = []
    num_str = ((38 - length) * '0') + num_str[2:]
    rv = []
    for i, digit in enumerate(mask_str):
        if digit == '0':
            if num_str[i] is None:
                rv.append(0)
            else:
                rv.append(int(num_str[i]))
        elif digit == '1':
            rv.append(int('1'))
        else:
            rv.append('0')
            X_indicies.append(36 - i - 1)

    ret = int(bin(int(''.join(map(str, rv)), 2) << 1), 2) >> 1
    additonal_sum_lst = list_combo(X_indicies)
    additonal_sum_lst.append(0)
    task2_ret = [ret + elt for elt in additonal_sum_lst]

    return task2_ret


def task1(inpt):
    dic = {}
    current_mask = None
    for line in inpt:
        key, _ , num = line.split()
        if key[1] == 'a':
            current_mask = num
        else:
            assert key[1] == 'e'
            dic_key = key[4:-1]
            dic[dic_key] = generate_number(current_mask, num)
    return sum(dic.values())


def task2(inpt):
    dic = {}
    current_mask = None
    for line in inpt:
        key, _ , num = line.split()
        if key[1] == 'a':
            current_mask = num
        else:
            assert key[1] == 'e'
            dic_key = key[4:-1]
            index_lst = generate_number_task2(current_mask, dic_key)
            for index in index_lst:
                dic[index] = int(num)
    return sum(dic.values())


if __name__ == "__main__":
    inpt = util.read_strs("inputs/day14_input.txt", '\n')
    tst = util.read_strs("inputs/day14_test.txt",'\n')
    
    print("TASK 1")
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)
    
    print("TASK 2")
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)
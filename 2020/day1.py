import util
import math
import time


def find_product(df_lst):
    '''
    find_product
    computes the product of the pair and triple of 
    elements in the list that sum to 2020

    Inputs:
    - df_lst - list of values

    0xx
    00x
    000
    Returns: Tuple with product of pair and triple
    '''
    n = len(df_lst)
    df_lst.sort()
    soln_1 = None
    soln_2 = None
    for i in range(n-1):
        for j in range(i+1,n):
            if (df_lst[i] + df_lst[j] == 2020):
                soln_1 = df_lst[i]*df_lst[j]
            elif (df_lst[i] + df_lst[j] > 2020):
                break
            for k in range(j+1, n):
                if (df_lst[i] + df_lst[j] + df_lst[k] == 2020):
                    soln_2 = df_lst[i]*df_lst[j] * df_lst[k]
                elif (df_lst[i] + df_lst[j] + df_lst[k] > 2020):
                    break
    return soln_1, soln_2

if __name__ == "__main__":
    inpt = util.read_ints("inputs/day1_input.txt")
    
    print("TASK 1 and 2")
    start = time.time()
    util.call_and_print(find_product, inpt)
    end = time.time()
    print(end-start)
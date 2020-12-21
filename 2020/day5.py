'''
Day 5
https://adventofcode.com/2020/day/5
'''
import util

def task1(boarding_passes):
    '''
    Finds the highest ticket id from a list of nearby boarding passes

    Inputs:
        boarding_passes (lst of strs): a list of all the nearby boarding passes
    
    Outputs: an integer representing the highest ticket id
    '''
    max_id = -1
    for boarding_pass in boarding_passes:
        row, col = read_boarding_pass(boarding_pass)
        ticket_id = 8 * row + col
        max_id = max(max_id, ticket_id)
    return max_id

def task2(boarding_passes):
    '''
    Finds your ticket id from a list of nearby boarding passes

    Inputs:
        boarding_passes (lst of strs): a list of all the nearby boarding passes
    
    Outputs: an integer representing your ticket id
    '''
    ticket_id_lst = []
    for boarding_pass in boarding_passes:
        row, col = read_boarding_pass(boarding_pass)
        ticket_id = 8 * row + col
        ticket_id_lst.append(ticket_id)
    ticket_id_lst = sorted(ticket_id_lst)
    for i, ticket_id in enumerate(ticket_id_lst):
        if ticket_id_lst[i+1] - ticket_id == 2:
            return ticket_id + 1
    print('ERROR')



def read_boarding_pass(boarding_pass):
    '''
    Reads in each boarding pass and identifies the row and column

    Inputs:
        boarding_pass (str): a string representing a boarding pass

    Output: row, col (both ints) the row and column of the seat for that 
        boarding pass
    '''
    row_lttr = boarding_pass[:7]
    col_lttr = boarding_pass[7:]
    row, col = "", ""
    for elt in row_lttr:
        if elt == "F":
            row += "0"
        elif elt == "B":
            row += "1"
    for elt in col_lttr:
        if elt == "L":
            col += "0"
        elif elt == "R":
            col += "1"
    row = int(row, 2)
    col = int(col, 2)
    return row, col





if __name__ == "__main__":
    tst_passes = util.read_strs("inputs/day5_test.txt", sep = "\n")
    boarding_passes_inpt = util.read_strs("inputs/day5_input.txt", sep = "\n")
    print("TASK 1")
    util.call_and_print(task1, tst_passes)
    util.call_and_print(task1, boarding_passes_inpt)

    print("\nTASK 2")
    util.call_and_print(task2, boarding_passes_inpt)


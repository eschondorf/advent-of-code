'''
Day 16
'''
import util
import csv
import pandas as pd

def task1(tickets, valid_range):
    '''
    Solver for task 1. Identifies the error rate and valid tickets

    Inputs:
        tickets (lst of lst of ints): All the valid tickets as determined by 
            task 1
        valid_range (lst of tuples): list of all bounds of all the ranges
        field_names (lst of strs): corresponding names to ranges
    
    Returns: 
        error_rate (int): The sum of all the integers that don't fit into any 
            field
        valid_tickets (lst of lst of ints): a list of tickets where every 
            column fits into some range
    '''
    error_rate = 0
    valid_tickets=[]
    for ticket in tickets:
        add_ticket = True
        for number in ticket:
            if not is_valid(number, valid_range):
                error_rate += number
                add_ticket = False
        if add_ticket:
            valid_tickets.append(ticket)
    return error_rate, valid_tickets


def task2(tickets, valid_range, field_names):
    '''
    Solver for task 2

    Inputs:
        tickets (lst of lst of ints): All the valid tickets as determined by 
            task 1
        valid_range (lst of tuples): list of all bounds of all the ranges
        field_names (lst of strs): corresponding names to ranges
    
    Returns: an integer containing the product of the six values on your ticket 
        that correspond to fields with the word departure
    '''
    valid_dict = {}
    for i,_ in enumerate(tickets[0]):
        valid_dict[i+1] = [name for name in field_names]
    num_fields = len(valid_range)
    for ticket in tickets:
        for pos, number in enumerate(ticket):
            for i in range(0, num_fields, 2):
                if not is_valid(number, valid_range[i: i+2]):
                    valid_dict[pos+1].remove(field_names[i//2])
    dict_lst = simplify_dict(valid_dict)
    to_multiply = []
    my_ticket = valid_tickets[-1]
    result = 1
    for key, value in dict_lst:
        if value[0].split()[0] == "departure":
            result *= my_ticket[key-1]
    return result


def simplify_dict(d):
    '''
    Recursive helper function that takes a dictionary and determines how to 
        each key to a unique value. Note this only works if one key has only one 
        value and, once you remove that value, another key only has one value 
        and so on.

    Inputs: d (dict): The dictionary mapping columns to potential field names

    Returns: list of tuples containing the column number and the field name it 
        maps to
    '''
    if len(d) == 1:
        return list(d.items())
    else:
        single_key = None
        single_value = None
        for key, value in d.items():
            if len(value) == 1:
                single_key = key
                single_value = value
                break
        d.pop(single_key)
        for key, value in d.items():
            if single_value[0] in value:
                value.remove(single_value[0])
        remaining_lst = simplify_dict(d)
        return remaining_lst + [(single_key, single_value)]
        

def is_valid(num, valid_range):
    '''
    Checks whether number is in any valid range

    inputs: num - an integer
            valid_range: a list of length 2 lists containing the valid ranges

    outputs: boolen
    '''
    for lb, ub in valid_range:
        if num >= lb and num <= ub:
            return True
    return False


def create_ranges(file):
    '''
    Creates a list of ranges for the fields.

    Inputs: 
        file (file): The file containing the ranges and field names

    Returns: rv (list of tuples): list containing tuples of (lb, ub)
    '''
    rv = []
    field = util.read_strs(file, sep = '\n')
    for line in field:
        words = line.split()
        int_1 = words[-3]
        int_2 = words[-1]
        intv_1, intv_2 = text_to_range(int_1), text_to_range(int_2)
        rv.append(intv_1)
        rv.append(intv_2)
    return rv


def text_to_range(intg):
    '''
    Splits str ranges into list with integers for lower  and upper bounds

    Inputs:
        intg (str): Not my best variable name, the string 'lb-ub'
    
    Returns: list of ints contaning lower bound and upper bound
    '''
    splt_intv = intg.split("-")
    return [int(splt_intv[0]), int(splt_intv[1])]


if __name__ == "__main__":
    # Read in data
    ranges = create_ranges("inputs/day16_inputranges.txt")
    test_ranges = [[1, 3], [5, 7], [6, 11], [33, 44], [13, 40],[45, 50]]
    test_tickets = [[7,3,47], [40,4,50], [55,2,20], [38,6,12]]
    df = pd.read_csv("inputs/day16_input.csv")
    nearby_tickets = df.values.tolist()
    util.call_and_print(task1, test_tickets, test_ranges)  
    util.call_and_print(task1, nearby_tickets, ranges)  
    names = ['departure location', 'departure station', 'departure platform',
        'departure track', 'departure date', 'departure time', 
        'arrival location', 'arrival station', 'arrival platform', 
        'arrival track', 'class', 'duration', 'price', 'route', 'row', 'seat', 
        'train', 'type', 'wagon', 'zone']

    answer, valid_tickets = task1(nearby_tickets, ranges)

    valid_tickets.append([89,139,79,151,97,67,71,53,59,149,127,131,103,
                            109,137,73,101,83,61,107])
    util.call_and_print(task2, valid_tickets, ranges, names)


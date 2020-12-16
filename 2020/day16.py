'''
Day 16
'''
import util
import csv
import pandas as pd

def task1(tickets, valid_range):
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
    valid_dict = {}
    for i,_ in enumerate(tickets[0]):
        valid_dict[i+1] = [name for name in field_names]
    num_fields = len(valid_range)
    print(valid_dict)
    for ticket in tickets:
        for pos, number in enumerate(ticket):
            for i in range(0, num_fields, 2):
                if not is_valid(number, valid_range[i: i+2]):
                    valid_dict[pos+1].remove(field_names[i//2])
    #print(valid_dict)
    inv = {}
    for key, val in valid_dict.iteritems():
        for val_val in val:
            inv[val_val] = inv.get(val_val, []) + [key]
    print(inv)
    rv = simplify_dict(inv)
    return rv
    
    '''
    for num_ticket, ticket in enumerate(tickets):
        for i, number in enumerate(ticket):
            field = is_valid(number, valid_range)
            valid_dict[field_names[field]] += [(i, num_ticket)]
    print(valid_dict)
    '''

def simplify_dict(d):
    if len(d) == 1:
        return [list(d.items())]
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

def is_valid_task2(num, one_field_range):
    for i, (lb, ub) in enumerate(one_field_range):
        if num >= lb and num <= ub:
            return True
    return False

def create_ranges(file):
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
    splt_intv = intg.split("-")
    return [int(splt_intv[0]), int(splt_intv[1])]



if __name__ == "__main__":
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
    my_ticket = [89,139,79,151,97,67,71,53,59,149,127,131,103,
                            109,137,73,101,83,61,107]
    cols = [7, 11, 12, 13, 16, 18]
    d = {1: ['a', 'b', 'd'], 2: ['b', 'c'], 3: ['a', 'b'], 4: ['a']}
    print(simplify_dict(d))

'''
Day 23
https://adventofcode.com/2020/day/23
Code for linked list amended from from https://realpython.com/linked-lists-python/#how-to-create-a-linked-list
'''
import util
from enum import Enum
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        nodes.append(str(node.data))
        node = node.next
        while node is not self.head:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_after(self, target_node, new_node):
        if not self.head:
            raise Exception("List is empty")
        next_node = target_node.next
        new_node.next = next_node
        target_node.next = new_node
        new_node.previous = target_node
        next_node.previous = new_node
        return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove_node(self, target_node):
        if not self.head:
            raise Exception("List is empty")

        if target_node == self.head:
            self.head = self.head.next
    
        previous_node = target_node.previous
        next_node = target_node.next
        previous_node.next = next_node
        next_node.previous = previous_node
        return

        raise Exception("Node with data '%s' not found" % target_node_data)



def task1(lst):
    '''
    Calculates result for first task

    Input:
        lst (lst of ints): the input sequence

    Outputs: an integer representing the ending circle starting from 1
    '''
    llist, d = create_linked_lst(lst, False)
    current_cup_node = llist.head
    for i in range(100):
        llist, d, current_cup_node = play_round_fast(
                                            llist, d, current_cup_node, 9)
    current_node = llist.head
    rv = []
    for i in range(9):
        rv.append(current_node.data)
        current_node = current_node.next
    for i, val in enumerate(rv):
        if val == 1:
            break
    rv_lst = list(rv[i+1:]) + list(rv[:i])
    num = int(''.join(map(str,rv_lst)))
    return num


def play_round(lst):
    '''
    Plays one round of the game using lists

    Input: 
        lst (lst of ints): the starting position of the cups
    
    Outputs: lst (lst of ints): the ending position after the round of the cups
    '''
    m = len(lst)
    current_cup = lst[0]
    next_three = lst[1:4]
    next_val = (current_cup - 2)%m + 1
    while next_val in next_three:
        next_val = (next_val - 2)%m + 1
    lst = [lst[0]] + lst[4:]
    for i, elt in enumerate(lst):
        if elt == next_val:
            lst = lst[:i+1] + next_three + lst[i+1:]
            break
    lst = lst[1:] + [lst[0]]
    return lst


def play_round_fast(llist, d, current_cup_node, m):
    '''
    Simulates one round of the game now using a dictionary and linked lists

    Inputs:
        llist (linked list): represents the current circle of the cups
        d (dict): maps cup number to the node representing the cup
        current_cup_node (node): the current cup
        m (int): the length of the list
    
    Outputs: the updated llist, dictionary (stays the same), and 
        next_round_current_cup (a node)
    '''
    current_cup = current_cup_node.data
    next_three = [current_cup_node.next, current_cup_node.next.next, current_cup_node.next.next.next]
    next_three_val = [node.data for node in next_three]
    for node in next_three:
        llist.remove_node(node)
    next_val = (current_cup - 2)%m + 1
    while next_val in next_three_val:
        next_val = (next_val - 2)%m + 1
    next_val_node = d[next_val]
    for i in range (3):
        node_to_add = next_three[2-i]
        llist.add_after(next_val_node, node_to_add)
    next_round_current_cup = current_cup_node.next
    return llist, d, next_round_current_cup


def task2(lst):
    '''
    Plays the task 2 simulation and returns the desired result

    Input:
        lst (lst of ints): the input sequence

    Outputs: an integer representing the product of the two cups after cup 1 
        after the simulation
    '''
    llist, d = create_linked_lst(lst, True)
    current_cup_node = llist.head
    for i in range(10000000):
        llist, d, current_cup_node = play_round_fast(llist, d, current_cup_node, 1000000)
    one_node = d[1]
    return one_node.next.data * one_node.next.next.data


def create_linked_lst(lst, extra):
    '''
    Creates the linked list and dictionary from a list

    Inputs: 
        lst (lst of ints): the input sequence
        extra (boolean): states if there are more than 10 cups

    Outputs: the linked list and a dictioary mapping cup values to nodes
    '''
    d = {}
    llist = LinkedList()
    first_node = Node(lst[0])
    llist.head = first_node
    prior_node = first_node
    next_node = None
    d[lst[0]] = first_node
    for elt in lst[1:]:
        next_node = Node(elt)
        d[elt] = next_node
        prior_node.next = next_node
        next_node.previous = prior_node
        prior_node = next_node
    if extra:
        for elt in range(10, 1000001):
            next_node = Node(elt)
            d[elt] = next_node
            prior_node.next = next_node
            next_node.previous = prior_node
            prior_node = next_node
    prior_node.next = first_node
    first_node.previous = prior_node
    return llist, d


if __name__ == "__main__":
    tst = [3,8,9,1,2,5,4,6,7]
    inpt = [7,1,6,8,9,2,5,4,3]
    print("TASK 1")
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)
    print("\nTASK 2")
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)
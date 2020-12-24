'''
Day 7
https://adventofcode.com/2020/day/7/answer
'''
import util


def task1(inpt):
    '''
    Calculates the number of bags that contain a "shiny gold bag"

    Inputs:
        inpt (lst of strs): the rules for each color bag

    Output: an integer, the number of bags containing at least one "shiny gold"
    '''
    num_bags = 0
    bags_dict = read_dict(inpt)
    mem_dict = {}
    for key in bags_dict.keys():
        if task_1_r(bags_dict, mem_dict, key):
            num_bags += 1
    return num_bags


def task_1_r(bags_dict, mem_dict, bag_color):
    '''
    Recursive helper function for task 1

    Inputs:
        bags_dict (dict): dictionary mapping bag color to lst of tuple 
            containing (int) number of times the sub bag appears and (str) the 
            color of the sub bag
        mem_dict (dict): dictionary containing if each bag color has been shown 
            to have a "shiny gold" bag in it already (not used in final version)
        bag_color (str): current color for step of the recursion

    Output: boolean stating if the bag contains a "shiny gold" bag somewhere 
        inside of it
    '''
    sub_bags = bags_dict[bag_color]
    if sub_bags == None:
        return False
    sub_bags_color = [color for num, color in sub_bags]
    for sub_color in sub_bags_color:
        if sub_color == 'shiny gold bag' or mem_dict.get(sub_color, False):
            #mem_dict[color] = True
            return True
    else:
        shiny_gold = False
        for sub_color in sub_bags_color:
            if task_1_r(bags_dict, mem_dict, sub_color):
                shiny_gold = True
                #mem_dict[color] = True
        return shiny_gold


def task2(inpt):
    '''
    Calculate the number of bags inside the shiny gold bag

    Input:
        inpt (lst of strs): the rules for each color bag
    
    Outputs: an integer, the number of bags inside the shiny gold bag
    '''
    bags_dict = read_dict(inpt)
    num_bags = task2_r(bags_dict, "shiny gold bag")
    return num_bags-1


def task2_r(bags_dict, color, num_color = 1):
    '''
    Recursive helper function for task 2, finds number of bags inside given bag

    Inputs:
        bags_dict (dict): dictionary mapping bag color to lst of tuple 
            containing (int) number of times the sub bag appears and (str) the 
            color of the sub bag
        color (str): a bag color
        num_color: the number of times the color appears inside its parent bag
    
    Outputs: an integer, the number of bags inside given bag
    '''
    if bags_dict[color] == None:
        return num_color
    else:
        rv = 0
        sub_bags = bags_dict[color]
        for num, sub_color in sub_bags:
            recursive_call = int(task2_r(bags_dict, sub_color, num))
            rv += (int(recursive_call) ) * int(num_color)
        return rv + int(num_color)


def read_dict(inpt):
    '''
    Takes the input and translates to a dictionary mapping bags to subrules

    Inputs:
        inpt (lst of strs): the rules for each color bag

    Outputs: a dictionary mapping bags to sub rules
    '''
    d = {}
    for line in inpt:
        key, value = line.split(" contain ")
        key = key[:-1]
        if value == "no other bags.":
            d[key] = None
        else:
            lst_values = value[:-1].split(",")
            for elt in lst_values:
                elt_lst = elt.strip().split(" ")
                num = elt_lst[0]
                bag = " ".join(x for x in elt_lst[1:])
                if bag[-1] == "s":
                    bag = bag[:-1]
                lst = d.get(key, [])
                lst.append((num, bag))
                d[key] = lst
    return d
            


if __name__ == "__main__":
    tst = util.read_strs("inputs/day7_test.txt", sep = "\n")
    inpt = util.read_strs("inputs/day7_input.txt", sep = "\n")
    print("TASK 1")
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)
    print("\nTASK 2")
    util.call_and_print(task2, tst)

    tst_2=["shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags."]

    util.call_and_print(task2, tst_2)
    util.call_and_print(task2, inpt)

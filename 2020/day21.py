'''
Day 21
'''
import util

def read_inpt(inpt):
    '''
    Reads in inputs from file

    Input:
        inpt (lst of str): the ingredient/allergens labels input
    
    Outputs: list of tuples where first element is set of ingredients and 
        second element is list of allergens
    '''
    rv = []
    for line in inpt:
        ingredients, allergens = line.split("(contains")
        ingredients = set(ingredients.split())
        allergens = allergens.strip(")").replace(",", "").split()
        rv.append((ingredients, allergens))
    return rv


def task1(inpt):
    '''
    Takes input and computes the number of times an ingredient without any 
        allergen appears

    Inputs:
        inpt (lst of str): the ingredient/allergens labels input
    
    Output: (int) the number of times an ingredient without any allergen 
        appears and the dictionary of allergens (for task 2)
    '''
    lst = read_inpt(inpt)
    allergens_dict = {}
    ingredients_lst = [] 
    for ingredients, allergens in lst:
        for allergen in allergens:
            current_set = allergens_dict.get(allergen, ingredients)
            allergens_dict[allergen] = ingredients.intersection(current_set)
        ingredients_lst += ingredients
    total_allergens = set()
    for val in allergens_dict.values():
        total_allergens = total_allergens.union(val)
    for ingredient in total_allergens:
        ingredients_lst = [ingr for ingr in ingredients_lst if ingr != ingredient]
    return len(ingredients_lst), allergens_dict


def task2(inpt):
    '''
    Takes input and computes a string containing each ingredient that contains 
        an allergen, listed in alphabetical order of the allergen

    Inputs:
        inpt (lst of str): the ingredient/allergens labels input
    
    Output: rv (str) a string containing each ingredient that contains 
        an allergen, listed in alphabetical order of the allergen
    '''
    _, allergens_dict = task1(inpt)
    for key, val in allergens_dict.items():
        allergens_dict[key] = list(val)
    lst = simplify_dict(allergens_dict)
    lst_of_allergies = sorted([allerg for allerg,_ in lst])
    ret_str = ""
    for allergy in lst_of_allergies:
        for alg, ingred in lst:
            if allergy == alg:
                ret_str += ingred[0]
                ret_str += ","
                break
    ret_str = ret_str[:-1]
    return ret_str


def simplify_dict(d):
    '''
    Recursive helper function that takes a dictionary and determines how to 
        each key to a unique value. Note this only works if one key has only one 
        value and, once you remove that value, another key only has one value 
        and so on.

    Inputs: d (dict): The dictionary mapping alergen to potential ingredients

    Returns: list of tuples containing the allergen and the ingredient it 
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




if __name__ == "__main__":
    tst = util.read_strs("inputs/day21_test.txt", sep = "\n")
    inpt = util.read_strs("inputs/day21_input.txt", sep = "\n")
    print("TASK 1")
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)

    print("\nTASK 2")
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)
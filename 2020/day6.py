'''
Day 6
https://adventofcode.com/2020/day/6
'''
import util


def num_unique_answers(group):
    '''
    Counts the number of unique answers in a group

    Inputs:
        group (str): a list of all of the groups and their answers

    Output: an integer, the number of unique answers in the group
    '''
    total_answers = set()
    for person in group.split("\n"):
        for answer in person:
            total_answers.add(answer)
    return len(total_answers)


def task1(inpt):
    '''
    Counts the number of unique answers from the input

    Inputs:
        inpt (lst of strs): a list of all of the groups and their answers

    Output: an integer, the number of unique answers
    '''
    tot_unique = 0
    for group in inpt:
        tot_unique += num_unique_answers(group)
    return tot_unique


def num_all_answer(group):
    '''
    Counts the number of common answers in a group

    Inputs:
        group (str): a list of all of the groups and their answers

    Output: an integer, the number of common answers in the group
    '''
    all_answer = set(group.split("\n")[0])
    for person in group.split("\n")[1:]:
        person_answer = set()
        person_answer = set(person)
        all_answer = all_answer.intersection(person_answer)
    return len(all_answer)


def task2(inpt):
    '''
    Counts the number of common answers from the input

    Inputs:
        inpt (lst of strs): a list of all of the groups and their answers

    Output: an integer, the number of common answers
    '''
    tot_all = 0
    for group in inpt:
        tot_all += num_all_answer(group)
    return tot_all


if __name__ == "__main__":
    groups_tst = util.read_strs("inputs/day6_test.txt", sep = "\n\n")
    groups = util.read_strs("inputs/day6_input.txt", sep = "\n\n")

    print("TASK 1")
    util.call_and_print(task1, groups_tst)
    util.call_and_print(task1, groups)

    print("\nTASK 2")
    util.call_and_print(task2, groups_tst)
    util.call_and_print(task2, groups)
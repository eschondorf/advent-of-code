'''
Day 4
https://adventofcode.com/2020/day/4
'''
import util

def task1 (inpt):
    '''
    Checks for number of valid passports by task 1 rules

    Inputs:
        inpt (lst of strs): the passports

    Returns: an integer, the number of valid passports
    '''
    num_valid = 0
    for line in inpt:
        needed = 0
        optional = 0
        line_lst = line.split()
        for field in line_lst:
            field_name, value = field.split(":")
            if field_name == "cid":
                optional += 1
            else:
                needed += 1
        if needed == 7:
            num_valid += 1
    return num_valid


def task2(inpt):
    '''
    Checks for number of valid passports by task 2 rules

    Inputs:
        inpt (lst of strs): the passports

    Returns: an integer, the number of valid passports
    '''
    num_valid = 0
    for line in inpt:
        needed = 0
        optional = 0
        line_lst = line.split()
        for field in line_lst:
            field_name, value = field.split(":")
            if field_name == "cid":
                optional += 1
            elif (field_name == "byr" and int(value) >= 1920 
                    and int(value) <= 2002):
                    needed += 1
            elif (field_name == "iyr" and int(value) >= 2010 
                    and int(value) <= 2020):
                needed += 1
            elif (field_name == "eyr" and int(value) >= 2020 
                    and int(value) <= 2030):
                needed += 1
            elif field_name == "hgt":
                units = value[-2:]
                ht = value[:-2]
                if unicode(ht).isnumeric():
                    ht = int(ht)
                else:
                    continue
                if ((units == "cm" and ht >= 150 and ht <= 193) or 
                    (units == "in" and ht >= 59 and ht <= 76)):
                    needed += 1
            elif field_name == "hcl":
                if value[0] == "#":
                    num_correct = 0
                    invalid = False
                    for digt in value[1:]:
                        if ((digt >= "0" and digt <= "9") or 
                            (digt >= "a" and digt <= "f")):
                            num_correct += 1
                        else:
                            invalid = True
                    if (not invalid and num_correct == 6):
                        needed += 1
            elif (field_name == "ecl" and 
                    value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                needed += 1
            elif (field_name == "pid" and len(value) == 9 
                    and unicode(value).isnumeric()):
                needed += 1
        if needed == 7:
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    inpt = util.read_strs("inputs/day4_input.txt", sep = "\n\n")
    tst = util.read_strs("inputs/day4_test_input.txt", sep = "\n\n")
    tst2_valid = util.read_strs("inputs/day4_test_valid.txt", sep = "\n\n")
    tst2_invalid = util.read_strs("inputs/day4_test_invalid.txt", sep = "\n\n")

    print("TASK 1")
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)

    print("\nTASK 2")
    util.call_and_print(task2, tst2_valid)
    util.call_and_print(task2, tst2_invalid)
    util.call_and_print(task2, inpt)
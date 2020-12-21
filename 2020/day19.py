'''
Day 19
https://adventofcode.com/2020/day/19

All credit for this solution goes to Borja Sotomayor. Without him I would be
trying to create all the valid passwords.
'''
import util
import lark


def create_lark_grammer(inpt):
    '''
    Turns the input rules into grammar that lark can understand

    Inputs:
        inpt (lst of strs): the list of rules

    Outputs: a string of the grammar rules
    '''
    grammar = ""
    for line in inpt:
        grammar_name = ""
        grammar_rule = ""
        name, rule = line.split(":")
        if name == '0':
            grammar_name = "start"
        else:
            grammar_name = "rule" + name
        rule = rule.strip()
        if rule[0] == '"':
            grammar_rule = rule
        elif "|" not in rule:
            rule = rule.split(" ")
            for task in rule:
                if task != " ":
                    grammar_rule += "rule" + task + " "
        else:
            sub_grammar_rule1, sub_grammar_rule2 = "", ""
            sub1, sub2 = rule.split(" | ")
            sub1 = sub1.split(" ")
            sub2 = sub2.split(" ")
            for task in sub1:
                if task != " ":
                    sub_grammar_rule1 += "rule" + task + " "
            for task in sub2:
                if task != " ":
                    sub_grammar_rule2 += "rule" + task + " "
            grammar_rule = sub_grammar_rule1 + "| " + sub_grammar_rule2
        grammar += grammar_name + ": " + grammar_rule.strip() + "\n"
    return grammar[:-1]


def task_solver(rules_inpt, passw_inpt):
    '''
    Runs lark on the grammar

    Inputs:
        rules_inpt (lst of str): The rules given
        passw_inpt (lst of str): the passwords to check
    
    Outputs: number (int) of valid passwords
    '''
    gram = create_lark_grammer(rules_inpt)
    parser = lark.Lark(gram)
    num_correct = 0
    for line in passw_inpt:
        try:
            parser.parse(line.strip())
            num_correct += 1
        except lark.exceptions.LarkError:
            pass
    return num_correct


if __name__ == "__main__":
    tst = util.read_strs("inputs/day19_tst.txt", sep = "\n")
    for i, val in enumerate(tst):
        if val == "":
            break
    tst_rules = tst[:i]
    tst_codes = tst[i+1:]

    inpt = util.read_strs("inputs/day19_input.txt", sep = "\n")
    for j, val in enumerate(inpt):
        if val == "":
            break
    inpt_rules = inpt[:j]
    inpt_codes = inpt[j+1:]


    print("TASK 1")
    util.call_and_print(task_solver, tst_rules, tst_codes)
    util.call_and_print(task_solver, inpt_rules, inpt_codes)

    task_2_rules = []
    for line in inpt_rules:
        if line == "8: 42":
            line = "8: 42 | 42 8"
        elif line == "11: 42 31":
            line = "11: 42 31 | 42 11 31"
        task_2_rules.append(line)
    print("\nTASK 2")
    util.call_and_print(task_solver, task_2_rules, inpt_codes)

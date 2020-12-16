'''
Utility functions for AoC 2020
These functions were developed by Borja Sotomayor
'''

import math
import copy


# File I/O

def read_ints(filename, sep=None):
    """
    Read integers from a file, separated by whitespace or by the
    specified separator.
    """
    strs = read_strs(filename, sep)
    return [int(x) for x in strs]

def read_strs(filename, sep = None):
    """
    Read strings from a file, separated by whitespace or by the
    specified separator.
    """
    with open(filename) as f:
        txt = f.read().strip()
        strs = txt.split(sep)    

    return strs


#Calling

def call_and_print(fn, *args):
    """
    Call a function with some parameters, and print the
    function call and the return value.
    """
    str_args = ", ".join(repr(arg) for arg in args)

    if len(str_args) > 20:
        str_args = str_args[:20] + "..."

    print("{}({}) = {}".format(fn.__name__, str_args, fn(*args)))


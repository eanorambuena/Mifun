from collections.abc import Iterable
import math, types
import numpy as np

def is_integer(x):
    return type(x) is int

def is__positive(x):
    return x > 0

def is_negative(x):
    return x < 0

def is_real(x):
    return type(x) in [int, float]

def universal_truth(x):
    return True

def universal_falsity(x):
    return False

def Constant1(x):
    return 1

def x(y):
    return y

def is_iterable(x):
    return (type(x) in [list, Iterable, range])

def for_function(x):
    f = x[0]
    iterable = x[1]
    initial_value = x[2]
    total = initial_value
    for i in iterable:
        total = f([i, total])
    return total

def for_domain_function(x):
    return callable(x[0]) and is_iterable(x[1])

def string_balance(string, chars = "()"):
    # Check if string is balanced in the string
    balance = 0
    for char in string:
        if char == chars[0]:
            balance += 1
        elif char == chars[-1]:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def symmetric_strip(string, chars = "()"):
    # Remove chars from the beginning and end of string if they are balanced in the string
    while (string[0] == chars[0]) and (string[-1] == chars[-1]) and string_balance(string, chars):
        new_string = string[1:-1]
        if not string_balance(new_string, chars):
            break
        string = new_string

    return string

def format_function(f, other, operation, domain = False):
    if domain:
        if " " in other.short_name and " " in f.name:
                name = f"({f.name}) {operation} ({other})"
        elif " " in other.short_name:
            name = f"{f.name} {operation} ({other})"
        elif " " in f.name:
            name = f"({f.name}) {operation} {other}"
        else:
            name = f"{f.name} {operation} {other}"
    else:
        if " " in other.name and " " in f.name:
                name = f"({f.name}) {operation} ({other})"
        elif " " in other.name:
            name = f"{f.name} {operation} ({other})"
        elif " " in f.name:
            name = f"({f.name}) {operation} {other}"
        else:
            name = f"{f.name} {operation} {other}"
    return name

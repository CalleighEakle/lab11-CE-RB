# https://github.com/CalleighEakle/lab11-CE-RB
# Partner 1: Ryan Bos
# Partner 2: Calleigh Eakle

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    raise ZeroDivisionError if a == 0 else b / a

def log(a, b):
    raise ValueError if a <= 0 else math.log(b, a)

def exp(a, b):
    return a ** b


def add(a, b):
    answer = a + b
    return answer
    pass

def subtract(a, b):
    answer = a - b
    return answer
    pass

def multiply(a, b):
    answer = a * b
    return answer
    pass

def log(a, b):
    if a < 0:
        print("LogarithmicError")
    else:
        answer = math.log(a, b)
        return answer
    pass

def exponent(a, b):
    answer = a ** b
    return answer
    pass

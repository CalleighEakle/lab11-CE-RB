# https://github.com/CalleighEakle/lab11-CE-RB
# Partner 1: Ryan Bos
# Partner 2: Calleigh Eakle

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
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



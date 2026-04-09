import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
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

def divide(a, b):
    if a == 0:
        print("ZeroDivisionError")
    else:
        answer = b / a
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

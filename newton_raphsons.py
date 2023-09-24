import math
import sympy as sp

#you can change the equation
def calculate_function(x):
    return x**2-2*x-2

#I calculated the derivative of the expression and then substituted the value that I passed in the function
def calculate_derivative(value):
    x = sp.symbols('x')
    derivative = sp.diff(x**2-2*x-2, x)
    derivative_value = derivative.subs(x, value)
    return derivative_value

def newton_raphsons(x0,count):
    while(count>0):
        function = calculate_function(x0)
        derivative = round(calculate_derivative(x0),4)
        x1 = round(x0 - (function/derivative), 4)
        print(
            f"x0: {x0} | x1: {x1} | fx0': {derivative} ")
        x0=x1
        count-=1
newton_raphsons(2.5,6)
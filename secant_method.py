import math
#change this to whatever equation you have been provided with
def calculate_function(x):
    y = 2 * math.cosh(x)*math.sin(x)-1
    return y

#the count parameter determines the number of iterations
def secant_method(x0, x1, count):
    while (count > 0):
        fx0 = round(calculate_function(x0), 5)
        fx1 = round(calculate_function(x1), 5)
        if (fx1-fx0 == 0):
            break
        x2 = round((x0*(fx1) - x1*(fx0))/(fx1-fx0), 5)
        fx2 = round(calculate_function(x2), 5)
        print(f"x0: {x0} | x1: {x1} | x2: {x2} | fx0: {fx0} | fx1: {fx1} | fx2: {fx2} |")
 
        x0 = x1
        x1 = x2
        count -= 1

secant_method(0.4,0.5,9)
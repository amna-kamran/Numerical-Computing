import math

# change this to whatever equation you have been provided with
def calculate_function(x):
    y= math.sin(x)-5*x+2
    return y
# the count parameter determines the number of iterations
def regular_falsi(x0, x1, count):
    while(count>0):
        fx0 = round(calculate_function(x0),5)
        fx1 = round(calculate_function(x1),5)
        x2 = round((x0*(fx1) - x1*(fx0))/(fx1-fx0), 5)
        fx2 = round(calculate_function(x2),5)

        print(
            f"x0: {x0} | x1: {x1} | x2: {x2} | fx0: {fx0} | fx1: {fx1} | fx2: {fx2} |")
        if(fx2 >0):
            x0=x2
        else: x1=x2
        count-=1
regular_falsi(0.4, 0.6, 6)
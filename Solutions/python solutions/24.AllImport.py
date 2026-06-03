import math
from math import *
def mathfunc(n):
    if not isinstance(n,(int,float)):
        print("Invalid Input")
    else:
        print("Square root function: ",int(math.sqrt(n)))
        print("Power function: ",int(math.pow(n,2)))
        print("Pi Function:",int(math.pi * math.pow(n,2)))
num=int(input("Enter number:"))
mathfunc(num)

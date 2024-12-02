#Name: Michael Buzzetta
#Pledge: I pledge my honor that I have abided by the Stevens honor system

"""
This function takes the input
and finds what it is multiplied by every integer below it
"""
def factorial(n):
    if n == 0:
        return 1
    elif(n<0):
        return ("Please enter a positive number")
    else:
        return n * factorial(n-1)


"""
This function take two input, and add them together
"""
from functools import reduce

def add(x, y):
    return x+y


"""
This fuction find the avarage value in a list,
using the previous add function
"""
def mean(L):
    if L==[]:
        return 0
    else:
        r=reduce(add,L)
        l=len(L)
        return r/l

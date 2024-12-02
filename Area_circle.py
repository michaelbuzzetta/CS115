from math import pi
def area_circle(r):
    """
    This cunction computes the area of the circle
    Input: positive integer r-radius of the circle
    Output: area of the circle
    """
    area = pi*r**2
    return area

def dbl(x):
    return 2*x

def evens():
    """ Produce a line of the first ten even numbers """
    singles = list(range(10))
    doubles = map(bdl, singles)
    return list(doubles)

from functools import reduce
def span(l):
    maxi = reduce(max, 1)
    mini = reduce(min, 1)
    return maxi-mini
    

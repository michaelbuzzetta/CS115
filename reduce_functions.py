from functools import reduce
def add(x, y):
    return x+y
def gauss(n):
    i = range(1, n+1)
    return reduce(add, 1)

def square(x):
    return x**2

def sumOfSquares(n):
    i = range(1, n+1)
    m = map(square, i)
    #return reduce(add, sqs)
    return reduce(add, map(square, range(1,n+1)))

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

def activity(t):
    if t>=75:
        return "Beach"
    elif t>= 50:
        return "Hike"
    else:
        return "That stinks"
        
def

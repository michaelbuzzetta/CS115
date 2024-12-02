from functools import reduce
#def dbl(x):
#    return 2*x

def dblList(i):
    return list(map(lambda number: 2*number, i))

#def s(x, y):
#    return x+y

#def power2(x):
#    return x**2

def sumOfSquares(n):
    x = map(lambda a:a**2, range(1, n+1))
    return reduce(lambda a,b:a+b, x)

#def is_even(x):
#    if x%2 ==0:
#        return True
#    else:
#        return False

def evens(i):
    return list(filter(lambda x: x%2==0, i))

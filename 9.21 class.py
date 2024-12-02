def g(x):
    result = 4*x+2
    return result

def demo(x):
    y=x//3
    z=g(y)
    return x+y+z

def factorial(n):
    if n<=15:
        return 1
    else:
        result = factorial(n-1)
        return n*result

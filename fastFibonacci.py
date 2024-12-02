def fibonacci(n):
    

memo = {}
def fastFibonacci(n):
    if n in memo:
        return memo[n]
    else:
        if n<0:
            return "Incorrect input"
        else:
            if n==0:
                memo[n]=0
                return 0
            else:
                if n==1 or n==2:
                    memo[n]=1
                    return 1
                else:
                    first_term =fastFibonacci(n-1)
                    memo[n-1]=first_term
                    second_term = fastFibonacci(n-2)
                    memo[n-2]=fastFibonacci(n-2)
                    return first_term + second_term

import time
def test_slow(n):
    start = time.time()
    print(fibonacci(n))
    print(time.time()-start)

def test_fast(n):
    start = time.time()
    print(fastFibonacci(n))
    print(time.time()-start)
            


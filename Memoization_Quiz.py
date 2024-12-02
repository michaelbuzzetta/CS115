'''
Created on 10/14/2022
@author:   Michael Buzzetta
Pledge:    I pledge my honor that I have abided by the stevens honor system
'''

memo={0:2,1:1,2:3,3:4,4:7,5:11}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[n]
    else:
        if n==0:
            return 2
        else:
            if n==1:
                return 1
            else:
                first=fast_lucas(n-1)
                memo[n-1]=first
                second=fast_lucas(n-2)
                memo[n-2]=second
                memo[n]=first+second
                return first+second
memo1={}

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if (amount,tuple(coins)) in memo1:
        return memo1[(amount, tuple(coins))]
    else:
        if amount == 0:
            return 0
        else:
            if coins==[]:
                return float("inf")
            else:
                if coins[0]>amount:
                    temp=fast_change(amount, coins[1:])
                    return temp
                else:
                    use=1+fast_change(amount-coins[0], coins)
                    lose=fast_change(amount, coins[1:])
                    memo1[(amount, tuple(coins[1:]))]=min(use, lose)
                    return min(use, lose)
            

                
# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))



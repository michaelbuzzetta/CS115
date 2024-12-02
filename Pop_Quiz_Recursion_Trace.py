# pop quiz

# Name: Michael Buzzetta
# Pledge I pleadge my honor that I have abided by the stevens honor system

# Question 1
# Implement this function so it works correctly.
# Use recursion  
# You may use the built-in max function, only to find the max of two numbers.
# Hint: The base case is a one-element list which you can check as len(L)==1.

def myMax(L):
    '''Assume L is a non-empty list of numbers.  Return the maximum value.'''
    if L==[]:
        return 0
    else:
        return max(L[0], myMax(L[1:]))


def test():
    '''Prints True for each successful test'''
    print( myMax([1,2,3]) == 3 )
    print( myMax([12,17,5,8,-100]) == 17 )
    print( myMax([12]) == 12 )

# Question 2
# Trace function call mystery(452)
def mystery(n):
    return m_help(n, 0)
def m_help(n, r):
    if n == 0:
        return r
    return m_help(n // 10, r * 10 + n % 10)
print(mystery(452)) # TRACE THIS

### Write your trace here
# The code begins in the mystery function, which takes one input,
# which calling the m_help function
# The m_help function takes two inputs, n and r.
# it then checks if n is 0, if it is, the function ends and prints out r,
# if it is not, the functionn continues
# m_help then takes n, divides it by 10 and rounds to the nearest whole number.
# it then multiplies r by 10 and adds it to the remainder of the
# new value for n divided by 10
# mystery is then called again and runs m_help to run those operations
# on the integer value of 452
###


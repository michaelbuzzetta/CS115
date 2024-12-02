# 11/10/2022
#Michael Buzzetta
#I pledge my honor that I have abided by the stevens honor system

from CS115 import * 

'''
This function uses a for loop to multiply c by n, without multiplocation
'''
def mult(c,n):
    result = 0
    for x in range(n):
        result = result+c
    return result

'''
This function takes the variable 'z' and updates
it with the formula z=z**2 +c n tines
'''
def update(c,n):
    z=0
    for x in range(n):
        z=z**2+c
    return z

'''
This function determines if c is in the set or not,
it returns true of it is and flase if it is not
'''
def inMset(c,n):
    z=0
    for x in range(n):
        z=z**2+c
        if abs(z)>2:
            return False
    return True
    

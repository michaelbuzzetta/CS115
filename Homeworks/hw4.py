'''
Created on October 17 2022
@author:  Michael Buzzetta
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - HW 4
'''

from functools import reduce 


'''
This is a helper function that computes the sum of two consecutive values of the list, and outputs a new list
'''
def nextItem(i):
    if len(i)==1:
        return []
    else:
        if len(i)==0:
            return 0
        else:
            newList = [i[0]+i[1]]+nextItem(i[1:])
            return newList
    
'''
This function takes an input, n, and returns a list of elements in n rows of the Pascal Triangle
'''
pascal_track = {0:tuple([1]), 1:(1,1)}
def pascal_row(n):
    if n in pascal_track:
        return list(pascal_track[n])
    else:
        if n<0:
            return []
        else:
            newList= nextItem(pascal_row(n-1))
            pascal_track[n] = tuple([1]+newList + [1])
            return [1]+newList+[1]


'''
This function takes as input a single integer n and returns a list of lists containing the values of the all the rows up to and including row n
'''
def pascal_triangle(x):
    if n==0:
        return [list(pascal_row(0))]
    else:
        return list(pascal_triangle(x-1))+[list(pascal_row(x))]

'''
This function performs tests on the pascal_row function. if there are no errors, it doesnot return anything
'''
def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(6) == [1, 6, 12, 12, 6, 1]
    

'''
This function performs tests on the pascal_triangle function. if there are no errors, it does not return anything
'''
def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1,3,4,3,1]]
    

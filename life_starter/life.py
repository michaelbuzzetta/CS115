#
# life.py - Game of Life lab
#
# Name: Michael Buzzetta
# Pledge:I pledge my honor that I have abided by the stevens honor system
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    '''
    returns a 2D array with the rows as height and collumns as width
    '''
    A=[]
    for row in range(height):
        A+=[createOneRow(width)]
    return A

def printBoard(A): 
    """
    this function prints the 2d list-of-lists 
    A without spaces (using sys.stdout.write) 
    """ 
    for row in A: 
        for col in row: 
            sys.stdout.write( str(col) ) 
        sys.stdout.write( '\n' ) 

def diagonalize(width,height): 
    """
    creates an empty board and then modifies it 
    so that it has a diagonal strip of "on" cells. 
    """ 
    A = createBoard( width, height ) 
     
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                A[row][col] = 1 
            else: 
                A[row][col] = 0      
    return A 
 
def innerCells(w,h):
    '''
    similar concpet to diagonalize
    '''
    A = createBoard(w,h)
    for row in range(h): 
        for col in range(w): 
            if col == 0 or row ==0: 
                A[row][col] = 0 
            else:
                if col == w-1  or row == h-1:
                    A[row][col]=0
                else:
                    A[row][col] = 1      
    return A 

def randomCells(w,h):
    '''
    similar concept to innerCells
    '''
    A = createBoard(w,h)
    for row in range(h): 
        for col in range(w): 
            if col == 0 or row ==0: 
                A[row][col] = 0 
            else:
                if col == w-1  or row == h-1:
                    A[row][col]=0
                else:
                    A[row][col] = random.choice([0,1])
    return A

def copy(A):
    '''
    This function creates a copy of a preexisting list
    '''
    h=len(A)
    w=len(A[0])
    B=createBoard(w,h)
    for row in range(h): 
        for col in range(w):
            B[row][col]=A[row][col]
    return B

def innerReverse(A):
    '''
    This function takes a pre existing list and flips 0 to 1 and 1 to 0,
    leaving the border alone
    '''
    h=len(A)
    w=len(A[0])
    for row in range(h): 
        for col in range(w): 
            if col == 0 or row ==0: 
                A[row][col] = 0 
            else:
                if col == w-1  or row == h-1:
                    A[row][col]=0
                else:
                    A[row][col] = 1-A[row][col]
    return A

def countNeighbors(rows,collumn,A):
    count=0
    for row in range(rows-1,rows+2):
        for col in range(collumn-1,collumn+2):
            if not(row==rows and col == collumn) and A[row][col]==1:
                count+=1

    return count
                

def next_life_generation(A):
    '''
    makes a copy of A and then advanced one 
        generation of Conway's game of life within 
        the *inner cells* of that copy. 
        The outer edge always stays 0. 
    '''
    newA=copy(A)
    h=len(newA)
    w=len(newA[0])
    for row in range(h): 
        for col in range(w): 
            if col == 0 or row ==0: 
                newA[row][col] = 0 
            else:
                if col == w-1  or row == h-1:
                    newA[row][col]=0
                else:
                    if countNeighbors(row, col, A)<2:
                        newA[row][col]=0
                    else:
                        if countNeighbors(row, col, A)>=3:
                            newA[row][col]=1
                        else:
                            if countNeighbors(row, col, A)==3 and newA[row][col]==0:
                                newA[row][col]=1
    return newA
                        
                        
            
    


    

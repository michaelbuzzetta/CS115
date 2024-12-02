"""
Michael Buzzetta
I pledge my honor that I have abided by the stevens honor system
"""

"""
This function takes two lists and multiplies the values in the same position
then adds everything together
"""
def dot(L,K):
    if L==[] or K==[]:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

"""
This function takes a string and breaks it up into its individual letters
"""
def explode(S):
    if S=="":
        return []
    else:
        return [S[0]]+explode(S[1:])
        
"""
This function find the first instance of a value in a list
or prints out the length
"""

def ind(e, L):
    if L==[] or L=="":
        return 0
    else:
        if L[0]==e:
            return 0

        return 1+ind(e,L[1:])

"""
This function removes all instances of a value
"""
def removeAll(e, L):
    if L==[]:
        return []
    if e == L[0]:
        return [] + removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])
    return L

def even(x):
    if x%2==0:
        return True
    else:
        return False

"""
This function filters out all even/odd numbers
depending on the parameter
"""
def myFilter(n,L):
    if L==[]:
        return[]
    elif(n(L[0]) == True):
        return [L[0]]+myFilter(n,L[1:])
    else:
        return myFilter(n,L[1:])

"""
This function reverses every value in a list, including other lists
"""
def deepReverse(L):
    if L==[]:
        return []
    elif(isinstance(L[-1], list)):
        return [deepReverse(L[-1])]+deepReverse(L[0:-1])
    else:
        return [L[-1]]+deepReverse(L[0:-1])

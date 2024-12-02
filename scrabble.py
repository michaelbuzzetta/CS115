import sys
from functools import reduce
# Be sure to submit hw2.py.  Remove the '_template' from the file name.
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
# Implement your functions here.

def letterScore(letter, scorelist):
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter,scorelist[1:])

def wordScore(S, scorelist):
    if S == "":
        return 0
    return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def searchDict(letter, dict):
    return list(filter(lambda x: x == letter, dict)) != []

def explode(S):
    """Returns a list comprised of the individual characters in string S"""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

def ind(e,L):
    """Returns the first index at which e is found in L"""
    if L == "" or L == []:
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])

def isItemInList(item,L):
    if L == []:
        return False
    elif len(L) == ind(item,L):
        return False
    return True

def removeItemFromList(ind,L):
    if L == []:
        return []
    return L[:ind] + L[ind+1:]

def wordFromRack(word,list2):
    if word == []:
        return list2
    elif word[0] in list2:
        word0lessList = removeItemFromList(ind(word[0],list2),list2)
        return wordFromRack(word[1:],word0lessList)
    else:
        return False

def test(word,list2):
    if word == [] or word == "":
        return list2
    elif word[0] in list2:
        word0lessList = removeItemFromList(ind(word[0],list2),list2)
        return test(word[1:],word0lessList)
    else:
        return False

def explodeDict(rack,dict):
    if dict == []:
        return []
    wordPossible = test(dict[0],rack)
    if wordPossible != False:
        return [dict[0]] + explodeDict(rack,dict[1:])
    else:
        return explodeDict(rack,dict[1:])

def wordScoreFromWord(word):
    return [word,wordScore(word,scrabbleScores)]

def scoreList(rack):
    explodedDict = explodeDict(rack,Dictionary)
    return list(map(wordScoreFromWord,explodedDict))

def keepDrop(origin):
    if origin == []:
        return ["",0]
    elif len(origin) <= 1:
        return origin[0]
    elif origin[0][1] < origin[1][1]:
        return keepDrop(origin[1:])
    else:
        concat = [origin[0]] + origin[2:]
        return keepDrop(concat)

def bestWord(rack):
    origin = scoreList(rack)
    return keepDrop(origin)

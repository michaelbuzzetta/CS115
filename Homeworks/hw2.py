
'''
Created on Sep 28
@author:   Michael Buzzetta
Pledge:    I pledge my honor that I have abided by the stevens honor system
CS115 - Hw 2
'''
from functools import reduce
import sys
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

'''
This function takes an input, letter, and returns the corersponding score
associated with that letter
'''
def letterScore(letter, scorelist):
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter,scorelist[1:])

'''
this function take an input, S and a scorelist, and it will return
scrabble score of that string as the output
'''
def wordScore(S, scorelist):
    if S == "":
        return 0
    return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

'''
This function seaches the dictiionary for a single letter word that you give it
'''
def dictSearch(letter, dict):
    return list(filter(lambda x: x == letter, dict)) != []

'''
This function checks if you can make a word with a series of inputed chars and returns true or false depending on its findings
'''
def wordMake(letters, word):
    if word=="":
        return True
    else:
        if (word[0] in letters):
            index = letters.index(word[0])
            letters=letters[0:index]+letters[index+1:]
            return(wordMake(letters,word[1:]))
        else:
            return False  

'''
This function takes an input, Rack, and checks it against the given dictionary to see if any words can be made, and returns the words and the score
'''
def scoreListHelper(Rack, dictionary):
    if Rack ==[]:
        return[]
    
    if dictionary==[]:
        return []
    else:
        if wordMake(Rack, dictionary[0]):
            x=dictionary[0]
            return [[x, wordScore(x,scrabbleScores)]]+scoreListHelper(Rack,dictionary[1:])
        else:
            return scoreListHelper(Rack,dictionary[1:])

'''
This function calls the helper function and returns the result
'''
def scoreList(Rack):
    return scoreListHelper(Rack, Dictionary)

'''
This function takes an input, Rack, and the result of scoreList and finds the best word to use
'''
def bestWordHelper(Rack, scoreList, maxScore):
    if scoreList==[]:
        return maxScore
    else:
        if scoreList[0][1]>maxScore[1]:
            return bestWordHelper(Rack, scoreList[1:], scoreList[0])
        else:
            return bestWordHelper(Rack, scoreList[1:], maxScore)

'''
This funtion calls the helper funtion and returns the result, while checking for a blank list
'''
def bestWord(Rack):
    sclt = scoreList(Rack)
    if sclt ==[]:
        return ['',0]
    return bestWordHelper(Rack, sclt[1:], [sclt[0][0], sclt[0][1]])
    

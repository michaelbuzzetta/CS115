'''
Created on 10/8/22
@author:   Michael Buzzetta
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
this function take an input, S and a scorelist, and it will return
scrabble score of that string as the output
'''
def wordScore(word, Scores, realScores):
    if word == '':
        return 0
    elif word[0] == Scores[0][0]:
        return Scores[0][1] + wordScore(word[1:], realScores, realScores)
    else:
        return wordScore(word, Scores[1:], realScores)

'''
This function returns all possible words and its corresponding score
'''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''

    if dct == []:
        return []

    else:
        return [[dct[0], wordScore(dct[0], scores, scores)]] + wordsWithScore(dct[1:], scores)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0 or L == []:
        return []
    else:
        return [L[0]] + take(n - 1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    elif n == 0:
        return L
    else:
        return drop(n-1, L[1:])


def bigIndex(coins):
    '''Returns the index of the largest coin'''
    if len(coins) <= 1:
        return 0
    elif coins[0] > coins[1]:
        return bigIndex([coins[0]] + coins[2:])
    else:
        return 1 + bigIndex(coins[1:])

'''
this function returns the smallest possible combo of coins
'''
def giveChangeHelper(amount, realAmount, coins):
    ind = bigIndex(coins)
    
    if amount == 0 or coins == []:
        return []
    elif coins[ind] > amount:
        return giveChangeHelper(amount, realAmount, coins[0:ind] + coins[ind+1:])
    else:
        use = [coins[ind]] + giveChangeHelper(amount - coins[ind], realAmount, coins)
        lose = giveChangeHelper(amount, realAmount, coins[0:ind] + coins[ind+1:])

        if sum(lose) != realAmount:
            return use
        else:
            if len(use) < len(lose):
                return use
            else:
                return lose

'''
returns the length of the smallest possible combo of coins
to make change, and the list itself
'''
def giveChange(amount, coins):
    best = giveChangeHelper(amount, amount, coins)

    return [len(best), best]


from test import *

class Tests():
    
    def __init__(self):
        self.tests = [
            {
                "func": giveChange,
                "possible_points": 15,
                "cmp": lambda x, y: x[0] == y[0] and set(x[1]) == set(y[1]),
                "tests": [
                    {
                        # "inputs" means that they are separate
                        # "input" (singular) means interpret a list as a single input 
                        "inputs": [400, [1, 9, 50, 392]],
                        "expected": [8, [50, 50, 50, 50, 50, 50, 50, 50]],
                        "points": 3 
                    },
                    {
                        "inputs": [32, [1, 5, 10, 25]],
                        "expected": [4, [1, 1, 5, 25]],
                        "points": 3 
                    },
                    {
                        "inputs": [32, [1, 7, 24, 42]],
                        "expected": [3, [1, 7, 24]],
                        "points": 3
                    },
                    {
                        "inputs": [48, [1, 5, 10, 25, 50]],
                        "expected": [6, [25, 10, 10, 1, 1, 1]],
                        "points": 3
                    },
                    {
                        "inputs": [48, [50, 25, 10, 5, 1]],
                        "expected": [6, [25, 10, 10, 1, 1, 1]],
                        "points": 3 
                    }
                ]
            },
            {
                "func": wordsWithScore,
                "possible_points": 15,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [Dictionary, scrabbleScores],
                        "expected": [['a', 1], ['am', 4], ['at', 2], ['apple', 9], ['bat', 5], ['bar', 5], ['babble', 12], ['can', 5], ['foo', 6], ['spam', 8], ['spammy', 15], ['zzyzva', 39]],
                        "points": 5
                    },
                    {
                        "inputs": [Dictionary, list(map(lambda x: [x[0], x[1]*2 + 1], scrabbleScores))],
                        "expected": [['a', 3], ['am', 10], ['at', 6], ['apple', 23], ['bat', 13], ['bar', 13], ['babble', 30], ['can', 13], ['foo', 15], ['spam', 20], ['spammy', 36], ['zzyzva', 84]],
                        "points": 5
                    },
                    {
                        "inputs": [["cats", "are", "cool"], scrabbleScores],
                        "expected": [['cats', 6], ['are', 3], ['cool', 6]],
                        "points": 5
                    }
                ]
            },
            {
                "func": take,
                "possible_points": 20,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [10, ["hello"]],
                        "expected": ["hello"],
                        "points": 5
                    },
                    {
                        "inputs": [3, [1, 2, 3, 4, 5]],
                        "expected": [1, 2, 3],
                        "points": 5
                    },
                    {
                        "inputs": [0, [52, 34]],
                        "expected": [],
                        "points": 5
                    },
                    {
                        "inputs": [1, ["a", "b", "c"]],
                        "expected": ["a"],
                        "points": 5
                    }
                ]
            },
            {
                "func": drop,
                "possible_points": 20,
                "cmp": lambda x, y: sorted(x) == sorted(y),
                "tests": [
                    {
                        "inputs": [10, ["hello"]],
                        "expected": [],
                        "points": 5
                    },
                    {
                        "inputs": [4, [1, 2, 3, 4, 5]],
                        "expected": [5],
                        "points": 5
                    },
                    {
                        "inputs": [0, ["a", "b", "c", "d"]],
                        "expected": ["a", "b", "c", "d"],
                        "points": 5
                    },
                    {
                        "inputs": [1, ["a", "b", "c"]],
                        "expected": ["b", "c"],
                        "points": 5
                    }
                ]
            }

        ]
memory_refresher = (
    "\n\n################ DONT FORGET ############\n"
    "## 5 points: Name, 5 points: Pledge    ##\n"
    "## 20 points: Docstrings  ##\n"
    "#########################################\n"
)

def test_answer(func, _input, expected, cmp, multi_input=False):

    try:
        # TODO: Only works for two inputs
        if multi_input:
            student_answer = func(_input[0], _input[1])
        else:
            student_answer = func(_input)
    except:
        raise RuntimeError("Oof, %s(%s) itself crashed :\\\n" % (func.__name__, _input))

    try:
        assert(cmp(student_answer, expected))
    except:
        print ("EXPECTED ANSWER: %s(%s) == %s" % (func.__name__, _input, expected))
        print ("STUDENT ANSWER:\t %s(%s) == %s" % (func.__name__, _input, student_answer))
        raise AssertionError("Yikes, their output was incorrect :(\n")


def run_all_tests():
    
    # We will sum these up as we go (variable possible points because some
    # assignments may have more or less than 100 points).
    possible_assign_points = 0
    final_assign_points = 0

    tests_ref = Tests()
    for test in tests_ref.tests:

        print("\n----------------------------------------------------------------------")
        print("Testing %s(): %s points" % (test["func"].__name__, test["possible_points"]))
        print("----------------------------------------------------------------------\n")

        for func_test in test["tests"]:
            try:

                # Check if we have "inputs" or "input". 
                # If it's "inputs", then use the different inputs 
                # If it's not, interpret input exactly as-is
                if "inputs" in func_test:
                    test_answer(test["func"], func_test["inputs"], func_test["expected"], test["cmp"], multi_input=True)
                else:
                    test_answer(test["func"], func_test["input"], func_test["expected"], test["cmp"])
                if "final_points" not in test:
                    test["final_points"] = 0
                test["final_points"] += func_test["points"]
            except (AssertionError, RuntimeError) as e:
                print (e)
        
        possible_assign_points += test["possible_points"]
        if "final_points" not in test:
            test["final_points"] = 0
        final_assign_points += test["final_points"]

        print ("%s/%s points" % (test["final_points"], test["possible_points"]))

    print ("\n\n##### TESTING COMPLETE ######")
    print ("## Final Code Score: %s/%s ##" % (final_assign_points, possible_assign_points))
    print ("#############################\n")

run_all_tests()

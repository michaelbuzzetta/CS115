'''
Created on 10/13
@author:   Michael Buzzetta
Pledge:    I pledge my honor that I have abided by the stevens honor system

CS115 - Lab 5
'''

import time


words = []
HITS = 10

def ED(first, second):
    """ Returns the edit distance between the strings first and second."""
    if first == '':
        return len(second)
    else:
        if second == '':
            return len(first)
        else:
            if first[0] == second[0]:
                return ED(first[1:], second[1:])
            else:
                substitution = 1 + ED(first[1:], second[1:])
                deletion = 1 + ED(first[1:], second)
                insertion = 1 + ED(first, second[1:])
                return min(substitution, deletion, insertion)

dic={}
'''
This function performs the same action as the previous function, but it tracks
its output to decrease the computing time for repeat inputs
'''
def fast_ED(first, second):
    if (first, second) in dic:
        return dic[(first, second)]
    if first == '':
        dic[(first, second)]=len(second)
        return len(second)
    else:
        if second == '':
            dic[(first, second)]=len(first)
            return len(first)
        else:
            if first[0] == second[0]:
                dic[(first, second)]=fast_ED(first[1:], second[1:])
                return fast_ED(first[1:], second[1:])
            else:
                substitution = 1 + fast_ED(first[1:], second[1:])
                deletion = 1 + fast_ED(first[1:], second)
                insertion = 1 + fast_ED(first, second[1:])
                minimum = min(substitution, deletion, insertion)
                dic[(first, second)]=minimum
                return minimum



def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).'''
    return list(map(lambda x: [fast_ED(x, user_input), x],words))
    #return map(lambda i: (fastED(user_input, words[i]), words[i]), range(0, len(words)-1))

def spam():
    '''If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()


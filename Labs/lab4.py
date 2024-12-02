'''
Michael Buzzetta
I pledge my honor that I have abided by the Stevens honor system
'''

from functools import reduce

'''
This function returns the vaule of the items in the knapsack
'''
def maxVal(n):
    if n ==[]:
        return 0
    else:
        return n[0][1] +maxVal(n[1:])


'''
This funtion returns the best combination of items from itemList
'''
def knapsackHelp(cap, itemList):
    if cap == 0:
        return []
    else:
        if itemList == []:
            return []
        else:
            if cap<itemList[0][0]:
                return knapsackHelp(cap, itemList[1:])
            else:
                useIt = [itemList[0]] + knapsackHelp(cap - itemList[0][0],
                                                   itemList[1:])

                loseIt = knapsackHelp(cap, itemList[1:])
                if maxVal(useIt)>maxVal(loseIt):
                    return useIt
                else:
                    return loseIt

'''
this function returns the items that the helper function deemed the best
'''
def knapsack(capacity, itemList):
    bestSack = knapsackHelp(capacity, itemList)
    return [maxVal(bestSack), bestSack]


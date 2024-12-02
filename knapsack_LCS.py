def knapsack(capacity, items):
    if len(items) == 0 or capacity <= 0:
        return 0
    elif items[0][0]>capacity:
        return knpasack(capacity, items[1:])
    else:
        use_it=items[0][1]+knapsack(capacity-items[0][0],items[1:])
        lose_it=knapsack(capacity,items[1:])
        return max(use_it,lose_it)

def LCS(s1,s2):
    if s1=="" or s2=="":
        return 0
    else:
        if s1[0]==s2[0]:
            return 1+LCS(s1[1:],s2[1:])
        else:
            return max(LCS(s1,s2[1:]), LCS(s1[1:], s2))

def distance(first, second):
    if first =="":
        return len(second)
    elif second=="":
        return len(first)
    elif first[0]==second[0]:
        return distance(first[1:], second[1:])
    else:
        sub=1+distance(first[1:],second[1:])
        

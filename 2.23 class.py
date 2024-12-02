def summation(l):
    if l==[]:
        return 0
    else:
        return l[0]+summation(l[1:])

def length(l):
    if l==[]:
        return 0
    else:
        return 1+length(l[1:])

def reverseList(l):
    if l==[]:
        return []
    else:
        return [l[-1]]+reverseList(l[:-1])

def reverseString(s):
    if s =="":
        return ""
    else:
        return reverseString(s[1:])+s[0]

def pascal(n,r):
    if n==1:
        return 1
    elif r==1 or r==n:
        return 1
    else:
        return pascal(n-1, r-1)+pascal(n+1,r)

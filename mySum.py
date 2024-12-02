def mySum(n):
    if n==[]:
        return 0
    else:
        return n[0]+mySum(n[1:])

def testmySum():
    assert mySum([1,2])==sum([1,2])

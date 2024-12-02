def multFive(x,a=[]):
    if x==[]:
        return a
    else:
        if x[0]%5==0:
            return multFive(x[1:],a+[x[0]])
        else:
            return multFive(x[1:],a)

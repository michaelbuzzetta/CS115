def andGate(a,b):
    if a==True and b==True:
        return True
    else:
        return False

def nandGate(a,b):
    if a==True and b==True:
        return False
    else:
        return True

def xorGate(a,b):
    if a !=b:
        return True
    else:
        return False

def orGate(a,b):
    if a==True:
        return True
    else:
        if b==True:
            return True
        else:
            return False

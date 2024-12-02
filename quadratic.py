'''
Michael Buzzetta
I pledge my honor that I have abided by the stevens honor system
Dec 1, 2022
'''

import math
from math import sqrt


class QuadraticEquation:
'''
This is a python script that will solve the quadratic equation
'''
    
    def __init__(self,a,b,c):
    '''
    this constructor gets the three values to be used
    '''
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
        if a==0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
    
    def getA(self):
    '''
    this function sets a
    '''
        return self.a

    
    
    def getB(self):
    '''
    this function sets b
    '''
        return self.b


    
    def getC(self):
    '''
    this function sets c
    '''
        return self.c
    
    def discriminant(self):        
    '''
this function checks if the value uner the square root is <0
    '''
        return (self.getB()**2)-(4*self.getA()*self.getC())

    
    def root1(self):
    '''
this function computes the quadratic equation with an addition
    '''
        if self.discriminant()>=0:
            return((self.getB()*(-1)+(sqrt((self.getB()**2)-(4*self.getA()*self.getC()))))/(2*self.getA()))
        else:
            return None

      
    def root2(self):
    '''
this function computes the quadratic equation with an subtraction
    '''  
        if self.discriminant()>=0:
            return((self.getB()*(-1)-(sqrt((self.getB()**2)-(4*self.getA()*self.getC()))))/(2*self.getA()))
        else:
            return None

    
    def __str__(self):
    '''
returns the quadratic equation in string form
    '''
        signOfA=""
        signOfB=""
        signOfC=""
        stringA=""
        stringB=""
        StringC=""
        if self.a<0:
            signOfA="-"
        if self.b<0 or self.c < 0:
            signOfB=" - "
        else:
            signOfB=" + "
        if self.c<0:
            signOfC=" - "
        else:
            signOfC=" + "
        if self.a==1 or self.a==-1:
            stringA=""
        else:
            stringA=str(abs(self.a))
        if self.b==0:
            StringA=""
        else:
            if self.b==1 or self.b==-1:
                stringB=signOfB+"x"
            else:
                stringB=signOfB+""+str(abs(self.b))+"x"
        if self.c==0:
            stringC=""
        else:
            stringC=signOfC+""+str(abs(self.c))+""
        return signOfA+stringA+"x^2"+stringB+stringC+" = 0"    

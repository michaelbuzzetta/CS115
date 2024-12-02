############################################################
# Name: Michael Buzzetta
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#  
############################################################
from math import factorial
from functools import reduce

def inverse(n):
    inv = float(1/n)
    return(inv)



'''
This function takes an imput, n, and creates a list and adds up all the values
and returns the sum
'''
def e(n):
    total = list(range(1,n+1))
    newList = [1] + list(map(factorials, total))
    return reduce(sum, map(inverse, newList))
    

def sum(x,y):
    return(x+y)

def factorials(z):
    return factorial(z)




import unittest
import Lab1 as lab1 #change lab1Solution with the name of your solution file
class Test(unittest.TestCase):
    def testInverse1(self):
        self.assertAlmostEqual(lab1.inverse(1), 1, 6)
    def testInverse2(self):
        self.assertAlmostEqual(lab1.inverse(2), 0.5, 6)
    def testInverse3(self):
        self.assertAlmostEqual(lab1.inverse(3), 0.3333333333333333, 6)
    def testInverse4(self):
        self.assertAlmostEqual(lab1.inverse(-3), -0.3333333333333333, 6)
    def testE1(self):
        self.assertAlmostEqual(lab1.e(1), 2, 6)
    def testE2(self):
        self.assertAlmostEqual(lab1.e(2), 2.5, 6)
    def testE3(self):
        self.assertAlmostEqual(lab1.e(10), 2.718281801146385, 10)
    def testE4(self):
        self.assertAlmostEqual(lab1.e(100), 2.7182818284590455, 10)
if __name__ == "__main__":
    unittest.main()

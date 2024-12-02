'''
Created on 10/20/22
@author:   Michael Buzzetta
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Lab 6
'''

'''
This function returns true of the inputed value is odd or false if the inputed value is even
'''
def isOdd(n):
    if n == 0:
        return False
    if n % 2 != 0:
        return True
    return False


'''
This functionon works if the inputed value is >0. It returns a string with the values
representing the non negative value in binary
'''
def numToBinary(n):
    if n == 0:
        return ""
    else:
        if isOdd(n):
            return numToBinary(n // 2) + "1"
        else: return numToBinary(n // 2) + "0"


'''
This function only works if s is comprised of only 0 and 1. It returns the integer equivilent
of the entered binary string
'''
def binaryToNum(s):
    if s == "":
        return 0
    return int(s[0])*(2**(len(s)-1)) + binaryToNum(s[1:])


'''
This function only works if s is a string of 8 bits. It returns a binary value of binaryToNum+1
'''
def increment(s):
    dec = binaryToNum(s)
    dec += 1
    answer = numToBinary(dec)
    if len(answer) > 8:
        return answer[(len(answer)-8):]
    answer = (8-len(answer))*"0" + answer
    return answer

'''
This function only works of s is 8 bit string and n greater than or equal to 0. it prints s and all
its successors to the nth value
'''
def count(s, n):
    if n == 0:
        print(s)
        return ""
    print(s)
    return count(increment(s), n-1)


'''
this function only works if n >=0. It returns the string containing the ternary representation of
non-negaitve integer 'n'
'''
def numToTernary(n):
    if n == 0:
        return ""
    return numToTernary(n // 3) + str(n % 3)

'''
This function only works of s is comprised of only 0, 1, and 2s. it returns the integer value that
corresponds to the ternary representation of s
'''
def ternaryToNum(s):
    if s == "":
        return 0
    return int(s[0])*(3**(len(s)-1)) + ternaryToNum(s[1:])


import unittest
import sys
import lab6
from io import StringIO
class Test(unittest.TestCase):
    def test01(self):
        self.assertEqual(lab6.isOdd(0), False)
        self.assertEqual(lab6.isOdd(1), True)
        self.assertEqual(lab6.isOdd(42), False)
        self.assertEqual(lab6.isOdd(43), True)
        self.assertEqual(lab6.isOdd(14312), False)
        self.assertEqual(lab6.isOdd(21617), True)
    def test02(self):
        self.assertEqual(lab6.numToBinary(0), '')
        self.assertEqual(lab6.numToBinary(1), '1')
        self.assertEqual(lab6.numToBinary(4), '100')
        self.assertEqual(lab6.numToBinary(10), '1010')
        self.assertEqual(lab6.numToBinary(42), '101010')
        self.assertEqual(lab6.numToBinary(100), '1100100')
        self.assertEqual(lab6.numToBinary(2587194), '1001110111101000111010')
    def test03(self):
        self.assertEqual(lab6.binaryToNum(''), 0)
        self.assertEqual(lab6.binaryToNum('0'), 0)
        self.assertEqual(lab6.binaryToNum('1'), 1)
        self.assertEqual(lab6.binaryToNum('100'), 4)
        self.assertEqual(lab6.binaryToNum('1011'), 11)
        self.assertEqual(lab6.binaryToNum('00001011'), 11)
        self.assertEqual(lab6.binaryToNum('101010'), 42)
        self.assertEqual(lab6.binaryToNum('1100100'), 100)
        self.assertEqual(lab6.binaryToNum('1001110111101000111010'), 2587194)
    def test04(self):
        self.assertEqual(lab6.increment('00000000'), '00000001')
        self.assertEqual(lab6.increment('11111111'), '00000000')
        self.assertEqual(lab6.increment('00000001'), '00000010')
        self.assertEqual(lab6.increment('00000111'), '00001000')
        self.assertEqual(lab6.increment('00101101'), '00101110')
        self.assertEqual(lab6.increment('11101101'), '11101110')
    def test05(self):
        # Reassign stdout for the duration of the test.
        saved_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            lab6.count('00010000', 0)
            self.assertEqual(
                sys.stdout.getvalue().strip(),
                '00010000')
            sys.stdout.close()
            sys.stdout = StringIO()
            lab6.count('00000000', 4)
            self.assertEqual(
                sys.stdout.getvalue().strip(),
                '00000000\n00000001\n00000010\n00000011\n00000100')
            sys.stdout.close()
            sys.stdout = StringIO()
            lab6.count('11111110', 5)
            self.assertEqual(
                sys.stdout.getvalue().strip(),
                '11111110\n11111111\n00000000\n00000001\n00000010\n00000011')
        finally:
            sys.stdout.close()
            sys.stdout = saved_stdout
    def test06(self):
        self.assertEqual(lab6.numToTernary(0), '')
        self.assertEqual(lab6.numToTernary(1), '1')
        self.assertEqual(lab6.numToTernary(4), '11')
        self.assertEqual(lab6.numToTernary(10), '101')
        self.assertEqual(lab6.numToTernary(42), '1120')
        self.assertEqual(lab6.numToTernary(100), '10201')
        self.assertEqual(lab6.numToTernary(2587194), '11212102222000')
    def test07(self):
        self.assertEqual(lab6.ternaryToNum(''), 0)
        self.assertEqual(lab6.ternaryToNum('1'), 1)
        self.assertEqual(lab6.ternaryToNum('11'), 4)
        self.assertEqual(lab6.ternaryToNum('101'), 10)
        self.assertEqual(lab6.ternaryToNum('1120'), 42)
        self.assertEqual(lab6.ternaryToNum('10201'), 100)
        self.assertEqual(lab6.ternaryToNum('11212102222000'), 2587194)
if __name__ == "__main__":
    unittest.main()

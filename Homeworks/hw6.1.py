'''
Created on 10/23/2022
@author:   Kieran Corson and Michael Buzzetta
Pledge:    I pledge on my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
k=5
# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

'''
This function is a helper function that tracks how many times the first value repeats
'''
def consecutive(s):
    if s=='':
        return 0
    else:
        if len(s)==1:
            return 1
        else:
            if s[0] == s[1]:
                return 1+consecutive(s[1:])
            else:
                return 1
           
'''
This helper function returns the intergers in succession in list format
'''
def successiveList(i):
    if i=='':
        return []
    return [consecutive(s)]+successiveList(i[consecutive(s):])

'''
This helper function ensures that the nummbers are not greater than the max run length,
and if they are larger than it breaks then up
'''
def lengthCheck(x):
    if x==[]:
        return []
    if x[0]>MAX_RUN_LENGTH:
        x[0]=x[0]-MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] +lengthCheck(x)
    return [x[0]]+lengthCheck(x[1:])
 
'''
This helper function determines whether an integer is even or odd
it returns false if the value is even and true of the value is odd
'''
def oddOrEven(a):
    if a==0:
        return False
    else:
        if a%2 ==1:
            return True
        else:
            return False

memo={}
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.
    Used in compress, compressHelp
    '''
    if n in memo:
        return memo[n]
    elif n==0:
        memo[n]=''
        return ''
    elif isOdd(n):
        x=numToBinary(int(n/2))+'1'
        memo[n]=x
        return x
    else:
        x=numToBinary(int(n/2))+'0'
        memo[n]=x
        return x

'''
This function checks that the binary number being returned is the correct length
and edits it if it is too short v
'''
def binaryLengthCheck(l):
    if len(l)>=COMPRESSED_BLOCK_SIZE:
        return l
    else:
        return binaryLengthCheck('0'+l)
   
   
'''
This function takes a binary string and returns a new binary string that
is the input's run-to-length encoding
'''
def compressHelp(t, m):
    if t == '':
        return ''
    else:
        if t[0]!= str(m):
            return '0' * COMPRESSED_BLOCK_SIZE + compressHelp(t, 1-m)
        else:
            x=consecutive(t)
            i=min(x, MAX_RUN_LENGTH)
            b=binaryLengthCheck(numToBinary(i))
            return b + compressHelp(t[i:], 1-m)

'''
This function returns the result from compressHelp
'''
#325 bits is the max
def compress(S):
    return compressHelp(S, 0)

def compression(s):
    """
    takes in the 64 length string
    returns the ratio of compressed size to original size
    """
    return len(compress(s))/len(s)

def isOdd(n):
    '''Returns whether or not the integer argument is odd.
    Used in numToBinary, uncompressHelper
    '''
    return n%2==1

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.
    Used in uncompressHelper
    '''
    if s=="":
        return 0
    else:
        return binaryToNum(s[0:-1])*2+(int(s[-1]))
   
def uncompressHelper(C, x):
    """
    Takes in length encoded C
    returns 64 length string s
    """
    if C=="":
        return C
    else:
        if x==1:
            return ("0"*(binaryToNum(C[:5])))+uncompressHelper(C[5:], 0)
        else:
            return ("1"*(binaryToNum(C[:5])))+uncompressHelper(C[5:], 1)

def uncompress(C):
    return uncompressHelper(C,1)
'''
I ran numerous random tests, such as "0"*64, "01"*64, "10"*64, "1000"*16.
The compression ratios were 0.390625, 5.0, 5.078125, and 2.578125 respectively
It is impossible for such an algorithm to exist because in the case of the maximum
sized image, it is not possible to return less than at least the image.
'''

# Demo of hmmm, the Harvey Mudd miniature machine
# D.Naumann 2015, rev Oct 2018

# When this file is loaded, it runs the program assigned
# to variable RunThis. Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.
# Remember to press F5 to run, after making changes.  

import sys
import importlib
# Also requires hmmmAssembler.py and hmmmSimulator.py to
# be available in the same directory as this file.


# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00read r1          #get input from user and store in r1
01read r2          #ditto, for r2
02 mul r3 r1 r2    #assign r3=r1*r2
03 write r3        #print r3
04 halt            #stops
"""


# Example2 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

Example2 = """
00 read r1
01 write r1
02 addn r1 1
03 jumpn 01
04 halt

"""

# AbsVal is a program that asks the user for
# an input and then prints its absolute value.

AbsVal = """
00 read r1
01 jgtzn r1 03
02 jltzn r1 05
03 write r1
04 halt
05 neg r1 r1
06 write r1
07 halt
 
"""

# StoreLoad is an example program that
#   1) asks the user for an input
#   2) stores the value in a memory location
#   3) increments it and stores in another location
#   4) loads from that location and writes that value
# Try changing 11 to the address of an instruction!

StoreLoad = """
00 read r1
01 storen r1 11
02 addn r1 1
03 setn r2 13
04 storer r1 r2
05 loadn r1 13
06 write r1
07 halt


"""

Triangle1 = """

"""

Triangle2 = """
00 read r1
01 read r2
02 mul r1 r1 r2
03 setn r2 2
04 div r1 r1 r2
05 write r1
06 halt

"""

Triangle3 = """
00 read r1
01 jeqzn r1 9
02 read r2
03 jeqzn r2 9
04 mult r3 r1 r2
05 setn r2 2
06 div r1 r1 r2
07 write r1
08 jumpn 0
09 halt

"""

Factorial = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

00 read r1
01 setn r13 1
02 jeqzn r1 7
03 mul r13 r13 r1
04 addn r1 -1
05 write r13
06 jumpn 2
07 halt

"""


# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = Factorial

# Choose whether to use debug mode; uncomment one of the following lines.
Mode = ['-n'] # not debug mode, 
#Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b



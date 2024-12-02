#11/3/2022
#Michael Buzzetta
#I pledge my honor that I have abided by the stevens honor system

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
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # assign r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Example2 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

Example2 = """
00 read r1          # get # from user to r1
01 write r1         # print the value of r1
02 addn r1 1        # add 1 to r1
03 jumpn 01         # jump to line 01
04 halt             # never halts! [use ctrl-c]
"""

# AbsVal is a program that asks the user for
# an input and then prints its absolute value.

AbsVal = """
00 read r1
01 jltz r1 4     # if r1 < 0 go to line 4
02 write r1      # print the absolute value
03 halt
04 setn r2 -1
05 mul r1 r1 r2  # assign r1 = r1 * -1 
06 jumpn 2       # go to line 2  
"""

# StoreLoad is an example program that
#   1) asks the user for an input
#   2) stores the value in a memory location
#   3) increments it and stores in another location
#   4) loads from that location and writes that value
# Try changing 11 to the address of an instruction!

StoreLoad = """
00 read r1         
01 storen r1 11   # put the value into mem[11]
02 addn r1 1       
03 setn r2 13 
04 storer r1 r2   # put incremented value into mem[13]
05 loadn r1 13
06 write r1       # write what was loaded
07 halt
"""

Triangle1 = """
00 read  r1          # get base
01 read  r2          # get height
02 mul   r1 r1 r2    # b times h into r1
03 setn  r2 2
04 div   r1 r1 r2    # divide by 2
05 write r1
06 halt
"""

Factorial = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

0       read    r1         # Get n
1       setn    r13 1      # initialize r13
2       jeqzn   r1 6       # done if r1 is 0
3       mul     r13 r13 r1 # change r13 = r13 * r1
4       addn    r1 -1      # change r1 = r1 - 1
5       jumpn   2          # repeat
6       write   r13
7       halt
"""

Fibonacci = """

00 read r2         #get n
01 setn r4 0       #initialize r4
02 setn r8 1       #initialoze r8
03 write r4        #print r4
04 write r8        #print r8
05 jeqzn r2 34     #if r2=0, move to end
06 jltzn r2 20     #if r2 <0, move to proper catch
07 addn r2 -1      #decrements r2 by 1
08 jeqzn r2 34     # if r2=0, move to end
09 addn r2 -1      #decrement r2 by 1
10 jeqzn r2 34     #if r2=0, move to end
11 add r4 r4 r8    #adds r4 and r8 and sets r4 equal to the result
12 write r4        #print r4
13 addn r2 -1      #decrement r2 by 1
14 jeqzn r2 34     #if r2=0, move to end
15 add r8 r8 r4    #adds r4 and r8 and sets r8 equal to the result
16 write r8        #prints r8
17 addn r2 -1      #decrement r2 by 1
18 jeqzn r2 34     #if r2=0, move to end
19 jumpn 11        #repeats the process until r2=0
20 neg r2 r2       #sets r2 to the invers of itself
21 addn r2 -1      #decrements r2 by 1
22 jeqzn r2 34     # if r2=0, move to end
23 addn r2 -1      #decrement r2 by 1
24 jeqzn r2 34     #if r2=0, move to end
25 add r4 r4 r8    #adds r4 and r8 and sets r4 equal to the result
26 write r4        #print r4
27 addn r2 -1      #decrement r2 by 1
28 jeqzn r2 34     #if r2=0, move to end
29 add r8 r8 r4    #adds r4 and r8 and sets r8 equal to the result
30 write r8        #prints r8
31 addn r2 -1      #decrement r2 by 1
32 jeqzn r2 34     #if r2=0, move to end
33 jumpn 25        #repeats the process until r2=0
34 halt            #end the program
"""

# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = Fibonacci

# Choose whether to use debug mode; uncomment one of the following lines.
# Mode = ['-n'] # not debug mode, 
Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b



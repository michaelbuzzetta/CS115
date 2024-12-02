#11/10/2022
#Michael Buzzetta
#I pledge my honor that I have abided by the stevens honor system
# mandelbrot.py
# Lab 9
#

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

'''
This function uses a 'for' loop to multiply c by n, without multiplication
'''
def mult(c,n):
    result = 0
    for x in range(n):
        result = result+c
    return result

'''
This function takes the variable 'z' and updates
it with the formula z=z**2 +c n tines
'''
def update(c,n):
    z=0
    for x in range(n):
        z=z**2+c
    return z

'''
This function determines if c is in the set or not,
it returns true of it is and false if it is not
'''
def inMSet(c,n):
    z=0
    for x in range(n):
        z=z**2+c
        if abs(z)>2:
            return False
    return True

'''
This function takes in four variables:
pix: integer representation of the pixel collumn
pixMax: total # of pixels available
floatMin: the lower endpoint of the images axis
floatMax: the upper endpoint of the images axis
'''
def scale(pix, pixMax, floatMin, floatMax):
    if pix==0:
        return floatMin
    else:
        if pix==pixMax:
            return floatMax
        else:
            x=(pix/pixMax)* (floatMax-floatMin)
            t=x+floatMin
            return t

'''
this function generates the width and height of a set of points in the Mandelbot set
it then creates a bitmap for it
'''
def mset(width=300, height=200): 
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height):
            x=scale(col,width, -2.0, 1.0)
            y=scale(row,height, -1.0, 1.0)
            # here is where you will need 
            # to create the complex number, c!
            c=x+(y*1j)
            n=15
            if inMSet(c,n) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile() 




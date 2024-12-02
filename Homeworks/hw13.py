#Michael Buzzetta
#I pledge my honor that I have abided by the stevens honor system
class Board
'''
    The game connect 4, in python
'''
    def __init__(self, width=7, height=6):
        '''
        THe constructor that creates the paramaters for the board
        '''
        self.col=width
        self.row=height
        self.array=[]
        row1=[]
        for r in range(height):
            for c in range(width):
                row1 += [" "]
            self.array+=row1
            row1=[ ]
                

    def __str__(self):
        '''This function prints the board'''
        x=""
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                x += ("|" + self.array[i][j]+ "|")
        return x

    def allowsMove(self, col):
        '''This function checks if the requested move is valid'''
        if col in range(self.col):
            if row[col]==" ":
                return True
            
    def addMove(self,col,ox):
        return True

    def setBoard(self, move_string):
        return True

    def delMove(self,col):
        return True

    def winsFor(self,col):
        return True

    def hostGame(self):
        return True
            

    

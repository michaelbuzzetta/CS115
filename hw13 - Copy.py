class Board():
    def __init__(self, width=7, height=6):
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
        x=""
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                x += ("|" + self.array[i][j]+ "|")
        return x

    def allowsMove(self, col):
        if col in range(self.col):
            if row[col]==" ":
                return True
        else:
            return False
            
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
            

    

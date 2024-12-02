class PointLine:
    def __init__(self, inputX, inputY):
        """ Assign inputX and input Y to the attributes x and y """
        self.x = inputX
        self.y = inputY
        
    def setXCoordinate(self, newX):
        """ Reset the value of the x-coodinate, if the new value of the x-coordinate
            is a decimal or integer. Print an error message otherwise.
        """
        if isinstance(newX,int) or isinstance(newX, float):
            self.x = newX
        else:
            print("The x-coordinate should be decimal or integer")

    def setYCoordinate(self, newY):
        """ Reset the value of the y-coodinate, if the new value of the y-coordinate
            is a decimal or integer. Print an error message otherwise.
        """
        if isinstance(newY,int) or isinstance(newY, float):
            self.y = newY
        else:
            print("The y-coordinate should be decimal or integer")

    def getXCoordinate(self):
        """ Return the x-coordinate of the point """
        return self.x

    def getYCoordinate(self):
        """ Return the y-coordinate of the point """
        return self.y

    def __repr__(self):
        """ Return a string representation of the point.
            For example for x = 2 and y = 3 we should get (2 , 3) back
        """
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __str__(self):
        """ Return a string representation of the point.
            For example for x = 2 and y = 3 we should get (2 , 3) back
        """
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        """ Returns True if two points are equal and False otherwise """
        return self.x == other.x and self.y == other.y

    
class Line:
    def __init__(self, Point1, Point2):
        """ Declare and initialize the 4 attributes of the class Line:
            Point1, Point2, slope and y-intercept
        """
        pass

    def getSlope(self):
        """ Return the slope of the line """
        pass
    
    def getYIntercept(self):
        """ Return the y-intercept of the line """

    def __repr__(self):
        """ Return a string representation of the line.
            For example, if slope = 1 and y-intercept=1, we should get 'y= 1x + 1' back
        """
        pass

    def __str__(self):
        """ Return a string representation of the line.
            For example, if slope = 1 and y-intercept=1, we should get 'y= 1x + 1' back
        """
        pass

    def __eq__(self, other):
        """ Returns True if two lines are equal and False otherwise """
        pass
    
    def parallel(self, other):
        """ Returns True if two lines are parallel and False otherwise """
        pass

    def intersection(self, other):
        """ Returns the intersection point of two lines """
        pass

    
    

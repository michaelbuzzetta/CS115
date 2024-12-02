class Rational:
    def __init__(self,n,d):
        self.numerator=n
        self.denominator=d

    def isZero(self):
        return self.numerator == 0

    def __str__(self): 
      return "Numerator " + str(self.numerator) + \
              " and Denominator " + str(self.denominator)

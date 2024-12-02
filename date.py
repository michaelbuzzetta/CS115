'''
Created on Dec 6 2022
@author:   Michael Buzzetta
Pledge:    I plege my honor that I have abide dby the stevens honor system
CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''
    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year
    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).
             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)
    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()
    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self): 
        '''Returns a new object with the same month, day, year 
           as the calling object (self).''' 
        dnew = Date(self.month, self.day, self.year) 
        return dnew

    def equals(self, d2): 
        '''Decides if self and d2 represent the same calendar date, 
            whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
        '''This function moves the date to the next day, checking if
            the month or year also change'''
        dim=DAYS_IN_MONTH[self.month]
        if dim==28 and self.isLeapYear()==True:
                dim=29
        if self.day+1<=dim:
               self.day=self.day+1
        else:
            self.day=1
            self.month = self.month+1
        if self.month>12:
            self.year=self.year+1
            self.month=1
        else:
            self.year=self.year
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def yesterday(self):
        '''This function tells you the date of yesterday, checking the month and year'''
        dilm=DAYS_IN_MONTH[self.month-1]
        if dilm==28 and self.isLeapYear()==True:
            dilm=29
        if dilm==0:
            dilm=DAYS_IN_MONTH[-1]
        if self.day-1>0:
            self.day=self.day-1
        else:
            self.day=dilm
            self.month=self.month-1
        if self.month==0:
            self.month=12
            self.year=self.year-1
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)
    def addNDays(self, N):
        '''This function adds an n anount of days to the given date'''
        print (self)
        for i in range(N):
            print(self.tomorrow())

    def subNDays(self, N):
        '''This functio an n anount of days to the given date'''
        print (self)
        for i in range(N):
            print(self.yesterday())

    def isBefore(self, d2):
        ''' This function checks if the second date is before the first date'''
        if d2.equals(self):
            return False
        else:
            if self.year>d2.year:
                return False
            else:
                if self.year==d2.year and self.month>d2.month:
                    return False
                else:
                    if self.year == d2.year and self.month == d2.month and self.day > d2.day:
                        return False
                    else:
                        return True

    def isAfter(self, d2):
        ''' This function checks if the second date is after the first one'''
        if d2.equals(self):
            return False
        else:
            if self.year<d2.year:
                return False
            else:
                if self.year==d2.year and self.month<d2.month:
                    return False
                else:
                    if self.year == d2.year and self.month == d2.month and self.day < d2.day:
                        return False
                    else:
                        return True

    def diff(self, d2):
        '''This function computes the total number of days in between two dates'''
        selfCopy=self.copy()
        d2Copy=d2.copy()
        total=0
        if self.equals(d2):
            return 0
        else:
            if selfCopy.isAfter(d2):
                while d2Copy.isBefore(self):
                    selfCopy.tomorrow()
                    total=total+1
                return total
            else:
                while selfCopy.isBefore(d2):
                    selfCopy.tomorrow()
                    total=total+1
                total=total*-1
                return total

    def dow(self):
        '''This function returns the day of the week'''
        givenDate=Date(4,20,2004)#This is my birthday and is a tuesday
        day=self.diff(givenDate)
        dayofWeek=day%7

        if dayofWeek==0:
            return "Tuesday"
        else:
            if dayofWeek==1:
                return "Wednesday"
            else:
                if dayofWeek==2:
                    return "Thursday"
                else:
                    if dayofWeek==3:
                        return "Friday"
                    else:
                        if dayofWeek==4:
                            return "Saturday"
                        else:
                            if dayofWeek==5:
                                return "Sunday"
                            else:
                                if dayofWeek==6:
                                    return "Monday"

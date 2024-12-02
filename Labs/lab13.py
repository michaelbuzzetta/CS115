'''
CS 115, Lab 13, Inheritance
Author: Michael Buzzetta
Pledge: I plege my honor that I have abided by the stevens honor system
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    '''Write getters for make, model, mpg, and tank_capacity.'''
    '''Write setters for mpg and tank_capacity.'''
    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def __init__(self, make, model, mpg, tank_capacity):
        self.__make=make
        self.__model=model
        self.__mpg=mpg
        self.__tank_capacity=tank_capacity

    def getMake(self):
        return self.__make
    def getModel(self):
        return self.__model
    def getMpg(self):
        return self.__mpg
    def getTankCapacity(self):
        return self.__tank_capacity

    def setMPG(self, x):
        return self.__mpg=x
    def setTankCapacity(self, t):
        return self.__tank_capacity=t

    def get_total_range(self):
        return "The car can travel " +self.__mpg*self.__tank_capacity +"miles on a full tank of gas"
    
    
    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    '''Implement the following method.'''

    def __init__(self, make, model, mpg, tank_capacity, batter_kWh, miles_per_kWh):
        self.__make=make
        self.__model=model
        self.__mpg=mpg
        self.__tank_capacity=tank_capacity
        self.__battery_kWh=battery_kWh
        self.__miles_per_kWh=miles_per_kWh
        
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''

        return "The car can travel "+self.__battery_kWh*self.__miles_per_kWh+"on a full charge"
 
    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''

    def get_total_range(self):
        return Car.get_total_range + HybridCar.get_battery_range
    
    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)

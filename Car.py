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
        '''This function creates a Car object'''
        self.__make=make
        self.__model=model
        self.__mpg=mpg
        self.__tank_capacity=tank_capacity

    def get_make(self):
        '''this function gets the make of the car'''
        return self.__make
    def get_model(self):
        '''this function gets the model of the car'''
        return self.__model
    def get_mpg(self):
        '''this function gets miles per gallon of the car'''
        return self.__mpg
    def get_tank_capacity(self):
        '''this function gets the tank capacity of the car'''
        return self.__tank_capacity

    def set_mpg(self, x):
        '''this function sets mpg to a value'''
        self.__mpg=x
        return self.__mpg
    def set_tank_capacity(self, t):
        '''this function sets tank cpacity to a value'''
        self.__tank_capacity=t
        return self.__tank_capacity

    def get_total_range(self):
        '''this function computes the total range of the car'''
        return self.__mpg*self.__tank_capacity
    
    
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

    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        '''this function creats a hybrid car object with the Car object as a base'''
        super().__init__(make, model, mpg, tank_capacity)
        self.__battery_kWh=battery_kWh
        self.__miles_per_kWh=miles_per_kWh
        
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''

        return self.__battery_kWh*self.__miles_per_kWh
 
    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''

    def get_total_range(self):
        '''this function computes the total range of the car bith both battery and gas'''
        return super().get_total_range() + self.get_battery_range()
    
    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)

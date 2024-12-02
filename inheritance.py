class Person:
    def __init__(self, first, last):
        self.firstName=first
        self.lastName=last

    def asleep(self, time):
        return 0<=time<=7

    def __str__(self):
        return self.firstName +" "+self.lastName

    def __eq__(self, other):
        return self.firstName==other.firstName and self.lastName==other.lastName

class Student(Person):
    def __init__(self, first, last, age):
        Person.__init__(self, first, last)
        self.age=age

    def asleep(self, time):
        return 0<=time<=9

    def __str__(self, other):
        return Person.__str__(self)+" asleep? "+str(self.asleep(self.age))

class Duck(Student):
    def _init_(self, first,last,age,dorm):
        Student.__init__(self,first,last, age)
        slef.dorm=dorm

    def asleep(self, time):
        return False

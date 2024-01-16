"""
Abstraction is one of the key principles of object-oriented programming (OOP) and refers to 
the concept of hiding the complex implementation details while exposing only the necessary 
functionalities or interfaces. It allows you to focus on what an object does rather than how
it achieves its functionality. In Python, abstraction is achieved through abstract classes 
and interfaces.


Abstract class: 
    -> A class which contain one or more abstract methods.
    -> Prevents the user to create an object of that class.
    -> Compels a user to override the abstract methods in a child class.
       child classes cannot miss the methods defined in abstract class.

Abstract method:
    -> A method that has a declaration but does not have an implementation.
    -> Abstract methods are declared without providing any implementation in the abstract 
       class, and they must be implemented by concrete (non-abstract) subclasses.

"""
        
from abc import ABC, abstractmethod

# Example 1
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    # if I add another method stop here which is not abstract method, then it's not necessary 
    # for the child classes to override it

    def stop(self):
        pass

class Bike(Vehicle):

    def go(self):
        print("You ride the bike")

    def stop(self):
        print("you stopped the bike")

class Car(Vehicle):
    
    def go(self):
        print("You Drive the car")

# it will create error because it must override the abstract method go from the parent class
# class Cycle(Vehicle):
#     pass

# vehicle = Vehicle()
# vehicle.go()
        
print("\nExample 1")
bike = Bike()
bike.go()
bike.stop()

car = Car()
car.go()

# car = Cycle()


# Example 2
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# shape = Shape()  # This would raise an error as abstract classes cannot be instantiated.
square = Square(4)
print("\nExample 2")
print(square.area())  # Output: 16


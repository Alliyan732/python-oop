"""
Polymorphism:
    --> Same function name (but different signatures) being uses for different types
                                    (or)
    --> Polymorphism is the ability of a single function or method to work in different 
        ways based on the context or the types of objects it operates on.

    -> It allows flexibility and code reuse

    -> For Example: A function calculating the length , If there is list it will return 
       length of the list, if there is string, it will return length of the string.

It includes:

    1) Function Overloading:
        -> Function overloading allows a class to define multiple methods withthe same name but with a different number or
           type of parameters.
        -> However, Python doesn't support traditional function overloading (as in some other languages like C++ or Java).
           In Python, you can achieve similar functionality using default parameter values or variable-length argument lists.

    2) Function Overriding:
        -> Function overriding occurs when a subclass provides a specific implementation for a method that is already defined 
           in its superclass.
        -> The overridden method in the subclass must have the same method signature (name and parameters) as the method in 
           the superclass.

"""

# 1) ------ Function Overloading ------ 
print('\nFunction Overloading Exampes')
# Example using Default Parameter Values:
class OverloadExample:
    def add(self, x, y=0):
        return x + y

obj = OverloadExample()
print('\nDefault Parameter Example')
print(obj.add(5))      # Output: 5
print(obj.add(5, 3))   # Output: 8


# Example using Variable-Length Argument Lists:
class OverloadExample:
    def add(self, *args):
        return sum(args)

obj = OverloadExample()
print('\nVariable-Length Argument Exampe')
print(obj.add(5))      # Output: 5
print(obj.add(5, 3))   # Output: 8


# 2) ------ Function Overriding ------ 

# Example 1 
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

square = Square(4)
print('\nFunction Overriding Exampe 1')
print(square.area())  # Output: 16

# Example 2
class Shape:
    def __init__(self, l, w):

        self.l = l
        self.w = w

    def calcArea(self):
        return self.l * self. w
        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    # overridden
    def calcArea(self):
        return 3.14 * super().calcArea()
        

print('\nFunction Overriding Exampe 2')
obj = Shape(3, 5)
print("Area of Rectangle: ", obj.calcArea())

obj2 = Circle(5)
print("Area of Circle: ", obj2.calcArea())


"""
Function Overriding:
    -> Function overriding occurs when a subclass provides a specific implementation for a method that is already defined 
       in its superclass.
    -> The overridden method in the subclass must have the same method signature (name and parameters) as the method in 
       the superclass.
"""

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


# method overriding in inheritance 
# It's a way to change the method in child class,  got from the parent class
# So the question is , why we Override method? 
# It's because we need to override method sometimes in realworld snarios,
# let's take a simple example that we have a parent class Shape, which has a function calc_area
# that takes 2 arguments length and width , and return the result as L*W for the area, 
# it's fine for the squares and rectangles , but waht if we have a child class circle?
# then we need to override the method for circle class , we all know the formula of 
# circle i.e Pi*r^2

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

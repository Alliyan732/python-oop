"""
Function Overloading:
    -> Function overloading allows a class to define multiple methods withthe same name but with a different number or
       type of parameters.
    -> However, Python doesn't support traditional function overloading (as in some other languages like C++ or Java).
       In Python, you can achieve similar functionality using default parameter values or variable-length argument lists.
"""

#  ------ Function Overloading ------ 
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
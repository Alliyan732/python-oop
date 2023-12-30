""" 
Access Modifiers

1. Public (default):
Members declared as public are accessible from outside the class.
In Python, all members of a class are public by default.

2. Protected (_ prefix):
Members declared as protected are accessible within the class and its subclasses.
Conventionally, a single leading underscore is added to the name to indicate that 
it should be treated as protected.

3. Private (__ prefix):
Members declared as private are accessible only within the class itself.
A double leading underscore is added to the name to make it private.

"""

# simple example of encapsualtion

class Person:
    
    _name = "Alliyan" # protected
    __age = 20        # private

    def show(self):
        print(f"Name is {self._name} and age is {self.__age}")


person = Person()
print(person._name) # it will print Alliyan beacause _name is a protected variable and can be called using class object.
# print(person.__age) # it will give error beacause __age is a private variable.

person.show()   # it will print both name and age beacause show is the public function that can access both variables
                # because it is in the same class.


""" Now understanding with subclasses """

class SuperClass:

    def __init__(self):
        self._name = "Alliyan"
        self.__age = 20
    
    # public function
    def show(self):
        return (self._name, self.__age)

# inherited class
class SubClass(SuperClass):
    def __init__(self):
        super().__init__()
        print(f"Getting protected variable from superclass: {self._name}")
        # print(f"Getting private variable from superclass: {self.__age}") 
        # it will give error bcz age is private

        print(super().show()) # it will print both bcz here we are calling public function show of super 
                              # class that has access to protected and private variables of the same class


obj = SubClass()
"""
Association is a fundamental concept in object-oriented programming (OOP) that describes a 
relationship between two or more classes. It represents how objects from different classes
interact with each other. 

Usage: 
    -> In some cases we can't use inheritance 
    -> for example we have salary and employee class, salary class contains the info about 
       the annual salary of employees. Can we apply "Inheritance" here?
       the answer is "No" because there is no inheritance relation here, salary is not the
       employee and employee is not the salary.

    

There are several types of associations, including:

1) Composition:

    -> Composition is a type os association where the contained class is part of the whole
       and cannot exist independently.
    -> In composition , we deligate some responsiblity from one class to another class
    -> It represents a "part-of" relationship.

    General Example:
        1) Suppose a house, compose of kitchen and bedrooms, here this type of association is
           composition because if the house burns down or collapses, kitchen and bedrooms will
           also burn. So the classes cannot exist independently.
        2) And if there will be a Chapter class, related to a Book, that would be composition.

2) Aggregation:

    -> Aggregation is a specific type of association where one class contains another class, 
       but the contained class can exist independently.
    -> It represents a "has-a" relationship.

"""

# ------ Composition ------

# Composition Example 1
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def calc_annualSalary(self):
        return (self.pay * 12) + self.bonus
    

# Employee class deligated some responsiblity to the Salary class 
class Employee:
    def __init__(self, name, age, type, pay, bonus):
        self.name = name
        self.age = age
        self.type = type
        self.pay = pay
        self.bonus = bonus

        # creating salary class object inside employee class
        self.salaryObj = Salary(pay, bonus)
        
    def calcSalary(self):
        return self.salaryObj.calc_annualSalary()

# here if we delete the Employee class instance, Salary class instance will automatically deleted
employee = Employee("Alliyan", 20, "Programmer", 150000, 20000)
print("\n------ Composition ------")
print("\nExample 1")
print("Employee's Annual Salary: ", employee.calcSalary())


# Example 2 (simple):
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car started")
        self.engine.start()

print("\nExample 2")
my_car = Car()
my_car.start()



# ------ Aggregation ------

# Aggregation Example 1
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def calc_annualSalary(self):
        return (self.pay * 12) + self.bonus
    

# Employee class deligated some responsiblity to the Salary class 
class Employee:
    def __init__(self, name, age, type, salary):
        self.name = name
        self.age = age
        self.type = type

        # creating salary class object inside employee class
        self.salaryObj = salary
        
    def calcSalary(self):
        return self.salaryObj.calc_annualSalary()

# Instead of using salary class inside the employee class , we have first created 
# the instance of salary class and then passed it to the employee constructor
# both the objects are independent of each other
salary = Salary(150000, 20000)
employee = Employee("Alliyan", 20, "Programmer", salary)
print("\n------ Aggregation ------")
print("\nExample 1")
print("Employee's Annual Salary: ", employee.calcSalary()) 


# Aggregation Example 2
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        print("Car started")
        self.engine.start()

print("\nExample 2")

# Creating an Engine instance separately
my_engine = Engine()


# Aggregation: Car has a reference to an Engine
my_car = Car(my_engine)
my_car.start()



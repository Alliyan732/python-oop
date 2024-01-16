
"""

"""
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass  # This method will be overridden by subclasses


# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"


# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"


# # Creating instances of the subclasses
# my_dog = Dog("Buddy")
# my_cat = Cat("Whiskers")

# # Using the inherited method
# print(my_dog.speak())  # Output: Buddy says Woof!
# print(my_cat.speak())  # Output: Whiskers says Meow!


# Example one

# class OttpSubscription():
#     def __init__(self, id, plan, amount):
#         self.id = id
#         self.plan = plan
#         self.amount = amount
    

#     def subscribe(self):
#         print(f"user with id: {self.id} has subscribed the {self.plan} plan")

#     def unSubscribe(self):
#         print(f"user with id: {self.id} has un-subscribed the {self.plan} plan")

# class PremiumSubscription(OttpSubscription):
#     def __init__(self, id, plan, amount, screens):
#         super().__init__(id, plan, amount)
#         self.screens = screens

#     def set_max_screens(self, screens):
#         self.screens = screens
#         print(f"Max screens set to {self.screens} in the premium plan")


# user1 = PremiumSubscription(123, "basic", 7000, 4)
# user1.subscribe()
# user1.set_max_screens(4)


# Example 2:

class Employee: 
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    # Print employees list
    def showEmployee(self):
        print(f"Employee: " )
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")


class Programmer(Employee):
    def __init__(self, name, age, salary, address, employeeType):
        self.employeeType = employeeType
        super().__init__(name, age, salary, address)
    
    # Print programmers list 
    def showProgrammer(self):
        print(f"\nProgrammer: " )
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")
        print(f"Employee Type: {self.employeeType}")
        

class Manager(Employee):
    def __init__(self, name, age, salary, address, employees):
        self.employees = employees
        # getting variables for super class Employee
        super().__init__(name, age, salary, address)
    
    # add employee in the manager's employees list'
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    # remove employee in the manager's employees list'
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    
    def shwoManagerEmployee(self):
        print(f"\nManager INfo: " )
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address} \n")
        
        for emp in self.employees:
            print(f"Manager's Employees: ")
            print("-->" , emp.name)
            


employee1 = Employee("Alliyan", 20, 150000, "Afshan Colony, RWP")
employee1.showEmployee()

programmer1 = Programmer("Alliyan", 20, 150000, "Afshan Colony, RWP", "Programmer")
programmer1.showProgrammer()

programmer2 = Programmer("Waqas", 21, 100000, "DHA, RWP", "Web Developer")
programmer2.showProgrammer()

manager1 = Manager("Alliyan", 20, 150000, "Afshan Colony, RWP", [])
manager1.add_employee(programmer1)
manager1.remove_employee(programmer1)
manager1.add_employee(programmer2)
manager1.shwoManagerEmployee()









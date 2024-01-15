
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

class OttpSubscription():
    def __init__(self, id, plan, amount):
        self.id = id
        self.plan = plan
        self.amount = amount
    

    def subscribe(self):
        print(f"user with id: {self.id} has subscribed the {self.plan} plan")

    def unSubscribe(self):
        print(f"user with id: {self.id} has un-subscribed the {self.plan} plan")

class PremiumSubscription(OttpSubscription):
    def __init__(self, id, plan, amount, screens):
        super().__init__(id, plan, amount)
        self.screens = screens

    def set_max_screens(self, screens):
        self.screens = screens
        print(f"Max screens set to {self.screens} in the premium plan")


user1 = PremiumSubscription(123, "basic", 7000, 4)
user1.subscribe()
user1.set_max_screens(4)










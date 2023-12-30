""" 
In Python, a decorator is a special type of function that is used to modify  
the behavior of another function or method. Decorators are often used to wrap or
extend the functionality of functions without modifying their code directly. 
Decorators are applied using the @decorator syntax above the function definition.
"""

def my_decorator(func):
    def wrapper():
        print("Hi")
        func()
        print("Thanks for using this function :)")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# When you call the decorated function, it includes the additional behavior defined in the decorator.
say_hello()

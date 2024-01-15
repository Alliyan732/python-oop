class Person:

    # constructor in a class gets automatically called when we create an object of the class
    
    # default constructor , if the constructor does not take arguments, then we call it default constructor
    # def __init__(self): 
    #     print("This is default constructor")


    # parameterize constructor
    def __init__(self, first_name, last_name, age): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        print("Person Info: ", self.first_name, self.last_name, self.age)
        

# person1 = Person()

person1 = Person("john", "smith", 24)
person2 = Person("Alliyan", "Waheed", 22)





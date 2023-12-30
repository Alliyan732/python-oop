class Person:
    first_name = ""
    last_name = ""
    age = 18
    def info(self):     # self parameter is a refference to the current instance of the class
        print("person info: ", self.first_name, self.last_name, self.age)


person1 = Person()

person1.first_name = "John"
person1.last_name = "smith"
person1.age = 24
person1.info()

person2 = Person()

person2.first_name = "alliyan"
person2.last_name = "waheed"
person2.age = 27
person2.info()

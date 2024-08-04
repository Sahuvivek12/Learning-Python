# Classes and objects in python

class Person:
    name = "Vivek"
    occupation = "Student"
    networth = "10"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()

a.name = "Vivek Sahu"
a.occupation = "Student"
a.info()
b.info()


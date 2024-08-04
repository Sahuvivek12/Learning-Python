# Constructors in python

class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occ = occupation

    def info(self):
        print(f"{self.name} is a {self.occ}")
        

a = Person("Vivek", "Student")
b = Person("Shivam", "Student")

a.info()
b.info()
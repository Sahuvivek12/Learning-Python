# Class methods as alternative constructors
class char:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def newname(cls, string):
        name, age = string.split("-")
        print(f"the name is {name} and the age is {age}")


char.newname("John doe-20")


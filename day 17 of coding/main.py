class Employee:
    def __init__(self, name, id) -> None:
        self.name  = name
        self.id = id

    def showDetails(self):
        print(f"{self.name}'s id is {self.id}")

class Programmer(Employee):
    def showLang(self):
        print("The default language is python")


a = Programmer("vivek", 444)

a.showDetails()
a.showLang()

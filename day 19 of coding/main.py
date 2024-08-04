# Class methods in python

class fruits:
    fruit = "banana"
    def basket(self):
        print(f"the name of the fruit is {self.fruit}")


    @classmethod
    def changeFruit(cls, newfruit):
        cls.fruit = newfruit
        print(newfruit)


a = fruits()
a.basket()
a.changeFruit("Apple")
a.basket()
print(fruits.fruit)
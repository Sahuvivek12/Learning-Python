# Single Inheritance

class Animal:
    def make_sound(self):
        print("Sound of an animal")


class Cat(Animal):
    def cats_sound(self):
        print("meow")


a = Animal()
b = Cat()

a.make_sound()
b.make_sound()
b.cats_sound()


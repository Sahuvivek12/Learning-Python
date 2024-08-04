# Static methods in python

# static methods can be used in a class without Self argument


class test:
    def __init__(self, num) -> None:
        self.num = num

    def addtoNum(self, n):
        n = self.num +n
        print(n)

    @staticmethod
    def add (a, b):
        print(a+b)


a = test(5)

a.addtoNum(5)

test.add(9, 20)
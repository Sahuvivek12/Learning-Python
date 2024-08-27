# generators in python

def gen():
    for i in range(5000000):
        yield i


g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
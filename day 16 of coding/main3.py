# Decorators in python

def greet(fx):
    def mfx(*args, **kwargs):
        print("Hey there!")
        fx(*args, **kwargs)
        print("thanks for using this funciton")
    return mfx


@greet   
def add(a, b):
    print(a+b)


add(3, 4)
# Map filter and Reduce
import functools as f
cube = lambda x: x*x*x


l = [1,3,4,6,6,5,4]


#MAP
newl = list(map(cube, l))

print(newl)


#FILTER

def filter_fx(a):
    return a>4

new2l = list(filter(filter_fx, l))
print(new2l)

def mysum(x, y):
    return x + y

sum = f.reduce(mysum, l)
print(sum)
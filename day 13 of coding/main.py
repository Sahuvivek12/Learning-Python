# Global and local variables
# local variables are those that are defined within a funciton, whereas Global variables are those defined outside of functions or globally.

x = 10 #Global variable
print(x)
def hello():
    global x #we can access global variables using the global function but it is generally a good practise to avoid using it
    x = 4
    y = 5 #Local variable
    print(y)
    print("Hello World")
    print(x)

hello()
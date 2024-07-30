# Finally keyword

# Finally keyword gets excuted regardless of the fact if the code block has a return line or not which wouldnt happen without the finally funciton

# def func1():
#     try:
#         l = [1, 4, 5 ,6]
#         int(input("enter a number: \n"))
#         return 1
        
        
#     except:
#         print("Error occured")
#         return 0

#     print("important code")

# x = func1()
# print(x)



# The part with print("important code") in the function does not get printed no matter which block 
# i.e try or except is excecuted in the function, but if we use the finally block,
#  that part can be exceuted and that is why we need finally block in python

def func1():
    try:
        l = [1, 4, 5 ,6]
        int(input("enter a number: \n"))
        return 1
        
        
    except:
        print("Error occured")
        return 0

    finally:
        print("important code")

x = func1()
print(x)


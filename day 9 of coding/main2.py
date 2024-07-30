# Exception Handling

try:
    a = int(input("please enter a number: \n"))
    for i in range (1,11):
        print(f"{a} x {i} = {a*i}")
    
except:
    print("Please enter a valid number")

# Raising Custom Errors

a = input("Enter a number between 5 and 9: \n")
if(a=="quit" or 5<=int(a)<=9):
    print("Good job")
else:
    raise ValueError("The value you entered is not between 5 and 9")
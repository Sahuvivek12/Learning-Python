# nested if-else-elif

a = int(input("Enter a number: \n"))

if (a<0):
    print("Number is negative")
elif(a>0):
    if(a<=10):
        print("Number is between 1-10")
    elif(a>10 and a<=20):
        print("Number is between 11-20")

else:
    print("Number is 0")



a = int(input("Enter the first number \n"))
b = int(input("Enter the second number \n"))
choice = int(input("Enter the number for operation you want to perform with the digits\n1. SUM\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n"))

if choice == 1:
    print ("Result : ",a+b)

elif choice == 2:
    print ("Result :",a-b)

elif choice == 3:
    print ("Result :", a*b)

elif choice == 4:
    print ("Result :", a/b)

else:
    print("Please enter a valid number for the operation")
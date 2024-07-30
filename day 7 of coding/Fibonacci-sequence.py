# f0 = 0
# f1 = 1
# f2 = f1+f0
# f(n)= f(n-1)+f(n-2)
try:

    a = int(input("Enter a number: \n"))

    def fibonacci(n):
        if (n==0 or n==1):
            return n
        else:
            return (fibonacci(n-1)+ fibonacci(n-2))

    for i in range(a+1):   
        print(fibonacci(i), end=" ,")

except:
    print("Please enter a valid number")

# Match-case

x = int(input("Enter a number: \n"))

match x:

    case 4:
        print("The number is 4")
    case 80:
        print("The number is 80")
    case _ if (x>8 and x<90):
        print("The number is between 9 and 89")
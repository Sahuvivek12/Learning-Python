l = ["What is the color of the sky? \n A. Red B. Green \n C. Blue D. Orange", 
    "Who is the prime minister of india?\n A. Narendra Modi B. Donald Trump \n C. Rahul Gandhi D. Rishi Sunak",
    "Where does a Shark live? \n A. Forest B. Clouds \n C. Apartments D. Ocean",
    "What is the name of the main character in DBZ? \n A. Goku B. Gohan \n C. Cell D. Yamcha",
    "What color is a Leaf? \n A. Blue B. Green \n C. White D. Pink"]

print("Welcome to kaun banega crorepati, here you can answer questions and win money,\n so get ready,\n heres your first question: \n")

print(l[0])

a = input("Enter the answer for question no. 1: \n")

if (a == "c" or a == "C"):
    print("Correct answer, You win 1,000 rupees \n")
    print(l[1])


    b = input("Enter the answer for question no. 2:\n")
    if(b == "a" or b == "A"):
        print("Correct answer again, you win 5,000 rupees \n")
        print(l[2])


        c = input("Enter the answer for question no 3:\n")
        if(c == "d" or c == "D"):
            print("WooHoo you win 10,000 rupees, this is a checkpoint \n")
            print(l[3])


            d = input("Enter the answer for question no. 4:\n")
            if(d == "a" or d == "A"):
                print("YOU WIN 50,000 RUPEES \n")
                print(l[4])

                e = input("Enter the answer for question no. 5: \n")
                if(e == "b" or e == "B"):
                    print("Excellent work! You Win 1,00,000 rupees")
                

                else:
                    print("Wrong answer, you can only take home 10,000 rupees, better luck next time")

            else:
                print("Wrong answer, sadly you lose all the money")
        else:
            print("Oops, wrong answer, 0 rupees won")

    else:
        print("That answer is incorrect, 0 rupees won")

else:
    print("Wrong answer, 0 rupees won")



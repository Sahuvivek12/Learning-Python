# KBC using loop

import random

questions = [
    [
        "What is the color of the sky?" , "Red" , "Green", "Blue", "Orange", "c"
    ],
    [
        "Who is the prime minister of india?", "Narendra Modi", "Donald Trump", "Rahul Gandhi", "Rishi Sunak", "a"
    ],
    [
        "What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "c"
    ],
    [
        "Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "b"
    ],
    [
        "What is the chemical symbol for gold?", "Au", "Ag", "Pb", "Fe", "a"
    ],
    [
        "Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", "b"
    ],
    [
        "What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "d"
    ],
    [
        "What is the boiling point of water in Celsius?" , "90°C" , "100°C" , "110°C" , "120°C" , "b"
    ],
    [
        "Which element has the atomic number 1?" , "Oxygen" , "Carbon" , "Hydrogen" , "Helium" , "c"
    ],
    [
        "Who is known as the 'Father of Computers'?" , "Charles Babbage" , "Alan Turing" , "Ada Lovelace" , "Grace Hopper" , "a"
    ],
    [
        "What is the smallest prime number?" , "0" , "1" , "2" , "3" , "c"
    ],
    [
        "Which continent is known as the 'Dark Continent'?" , "Asia" , "Africa" , "Europe" , "South America" , "b"
    ],
    [
        "What is the chemical formula for water?" , "CO2" , "H2O" , "O2" , "NaCl" , "b"
    ],
    [
        "Which planet is closest to the sun?" , "Venus" , "Earth" , "Mercury" , "Mars" , "c"
    ],
    [
        "What is the primary ingredient in guacamole?" , "Avocado" , "Tomato" , "Onion" , "Pepper" , "a"
    ],
    [
        "Which of these animals is known for its ability to change color?", "Elephant", "Chameleon", "Giraffe", "Lion", "b"
    ]
    ]


levels = [1000, 2000,3000, 5000, 10000, 20000,40000, 80000, 160000,320000, 640000,1250000, 2500000, 5000000,7500000,10000000]
money = "0"
try:
    for i in range (0, len(questions)):
        question = questions[i]
        print(f"\n\nQuestion no. {i + 1} for rupees {levels[i]} is\n{question[0]}")
        print(f"A. {question[1]}       B.{question[2]}")
        print(f"C. {question[3]}       D.{question[4]}")
        

        reply = (input("choose an option from (A, B, C, D) or enter 0 to quit: \n")).lower()

        if(reply == "quit" or reply=="0"):
            print("You have decided to quit the game")
            break


        if(i==1 and reply == "c"):
                print("Seriously dude? Rahul Gandhi? Wow...")

        if(reply == (question[5])):
            print(f"Correct answer you have won Rs. {levels[i]} ")

            


            if (i ==4):
                money = "10,000"
            elif (i ==9):
                money = "3,20,000"
            elif (i == 14):
                money = "1,00,00,000"

        else:
            print("Wrong answer")
            break
except:
    print("The game has ended")

print(f"\n\nYou will be taking home {money} rupees with you")

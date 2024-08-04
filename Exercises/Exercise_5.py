import random

l = ("rock","paper","scissors")

computer = random.choice(l).lower()
player = input("Sect rock, paper or scissors: \nYou:").lower()
print(f"Comp:{computer}\n\n")

if (computer == player):
    print("DRAW")
elif (computer == "rock" and player =="paper"):
    print("WIN")
elif(computer == "paper" and player == "scissors"):
    print("WIN")
elif(computer == "scissors" and player == "rock"):
    print("WIN")
else:
    print("LOSS")

if(player!="rock" and player!="paper" and player!="scissors"):
    print("Please enter a valid choice")
    

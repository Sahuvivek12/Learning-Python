import random

l = ("rock","paper","scissors")

computer = random.choice(l).lower()
player = input("Sect rock, paper or scissors: \nYou:").lower()
print(f"Comp:{computer}\n\n")

if (computer == player):
    print("DRAW")
if (computer == "rock" and player =="paper"):
    print("WIN")
if (computer == "rock" and player == "scissors"):
    print("LOSS")
if (computer == "paper" and player == "rock"):
    print("LOSS")
if(computer == "paper" and player == "scissors"):
    print("WIN")
if(computer == "scissors" and player == "rock"):
    print("WIN")
if(computer == "scissors" and player == "paper"):
    print("LOSS")


if(player!="rock" and player!="paper" and player!="scissors"):
    print("Please enter a valid choice")
    

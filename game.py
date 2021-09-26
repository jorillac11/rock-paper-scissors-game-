# game.py

import random
import os
from dotenv import load_dotenv

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the "python-dotenv" package docs for more info

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable

print (f"Welcome '{PLAYER_NAME}' this is my rock, paper, scissors game!")

#PROMPT USER FOR INPUT

#x = input ("Choose 'rock' or 'paper or 'scissors')
user_choice = input("Choose 'rock' or 'paper' or 'scissors'")
options = ["rock", "paper", "scissors"]

print("The user chose:")
print(user_choice)


if user_choice not in options:
    print("User did not make a valid choice")
    print("Try again, selecting either 'rock', 'paper', or 'scissors'")
    quit()

#COMPUTER CHOICE (AT RANDOM)
computer_choice = random.choice (options)

print("Computer chose:")
print(computer_choice)

#adapted from code share from Basil Bseiso in https://georgetown-py.slack.com/archives/C02BNKRKZV5/p1632240321010500
if(user_choice == "rock" and computer_choice == "scissors"):
    print("Congratulations,you win!")
elif(user_choice == "rock" and computer_choice == "paper"):
    print("Oh, the computer won. It's ok, try again.")
elif(user_choice == "paper" and computer_choice == "scissors"):
    print("Oh, the computer won. It's ok, try again.")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("Congratulations,you win!")
elif(user_choice == "scissors" and computer_choice == "rock"):
    print("Oh, the computer won. It's ok, try again.")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations,you win!")
else: print("It's a tie!")


print("THANKS, PLEASE PLAY AGAIN")

quit()

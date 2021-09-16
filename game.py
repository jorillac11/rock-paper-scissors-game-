# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

#PROMPT USER FOR INPUT

#x = input ("Choose 'rock' or 'paper or 'scissors')
user_choice = input("Choose 'rock' or 'paper' or 'scissors'")
print(user_choice)

#COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

print("Computer chose:")
print(computer_choice)

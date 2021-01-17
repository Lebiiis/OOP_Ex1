# File: Ex1_8
# Author: Niki Leppänen
# Description:  Code a simple (and textual) implementation of Rock-Paper-Scissors game. Best of 3 games wins.

# Necessary imports

import random

# Scoreboard

userwins = 0
compwins = 0


# Function for game

def game(u, c):
    if u == 1 and c == 3 or u == 2 and c == 1 or u == 3 and c == 2:
        return "User wins"
    elif u == 3 and c == 1 or u == 1 and c == 2 or u == 2 and c == 3:
        return "Comp wins"
    else:
        return "Tie"


# Use while loop to keep the game going

while True:

    # user and computer inputs

    user = int(input("Choose (1)Rock, (2)Paper or (3)Scissors "))
    comp = random.randint(1, 3)

    if game(user, comp) == "User wins":
        userwins += 1
        print("User wins")
        print(" User: ", userwins, "\n Computer: ", compwins)
    elif game(user, comp) == "Comp wins":
        compwins += 1
        print("Computer wins")
        print(" User: ", userwins, "\n Computer: ", compwins)
    else:
        print("It's a tie")
        print(" User: ", userwins, "\n Computer: ", compwins)

    play = input("Play again? [Y/N]: ")

    # Ask if user wants to play more

    if play == "N":
        break

# File: Ex2_7
# Author: Niki Leppänen
# Description:  Take a look at the coin.py, write it down in your IDE and run it. See that coin gets tossed.

import random


class Coin:

    # The __init__ method initializes the sideup data attribute with "Heads"
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generate a random number
    # int the range of 0 through 1. If the number = 0, then sideup is set to "Heads", otherwise sideup is set tu "Tails.
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value referenced by sideup.
    def get_sideup(self):
        return self.sideup


# The main function
def main():

    # Create an object from the Coin class.
    my_coin = Coin()
    # your_coin = Coin()

    # Display the side of the coin that is facing up.
    print("This side is up: ", my_coin.get_sideup())

    # Toss the coin.
    print("I am tossing the coin ...")
    my_coin.toss()

    # Display the  side of the coin that is facing up.
    print("This side is up: ", my_coin.get_sideup())


# Call the main function
main()

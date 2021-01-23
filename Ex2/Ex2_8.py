# File: Ex2_8
# Author: Niki Leppänen
# Description:  Modify the toss_the_coin()function so that there are 2more options: Coin lands on the table upright
# (and not flat showing heads or tails) or coin drops on the ground and disappears(on a rabbit hole).
# Name the options properly and give informative and readable output of the status.

import random


class Coin:

    # The __init__ method initializes the sideup data attribute with "Heads"
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generate a random number
    # int the range of 0 through 1. If the number = 0, then sideup is set to "Heads", otherwise sideup is set tu "Tails.
    def toss(self):

        coin_side = random.randint(0, 3)

        if coin_side == 0:
            self.sideup = 'Heads'
        elif coin_side == 1:
            self.sideup = 'Tails'
        elif coin_side == 2:
            self.sideup = 'Coin lands upright'
        else:
            self.sideup = 'Coin falls on the ground and was never found'

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

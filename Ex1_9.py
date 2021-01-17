# File: Ex1_9
# Author: Niki Leppänen
# Description:  Code a function that returns a random number between 1-6 when calling it.
#               Print out the number where the function is called (so do not print the number inside the function).
#               Name the function properly (see style guide).

# Necessary imports

import random


# Function for random number

def random_number_from_1_to_6():
    num = random.randint(1, 6)
    return num


# Print the results

print(random_number_from_1_to_6())


# File: Ex1_4
# Author: Niki Leppänen
# Description:  Write a program which repeatedly reads integers until the user enters 0. Print out the number of
#               negative integers. Use functions in your solution.


def ask_user():
    print("Write a number, 0 will stop the loop.")
    negative = 0

    while True:
        number = int(input())

        if number == 0:
            print("Amount of negative inputs: ", negative)

            return
        elif number < 0:
            negative += 1
            print(number)
        else:
            print(number)


ask_user()

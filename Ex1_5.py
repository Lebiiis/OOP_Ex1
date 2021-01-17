# File: Ex1_5
# Author: Niki Leppänen
# Description:  Add a function to the previous task that counts the number of even integers that were among the entered.

def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return


def ask_user():
    print("Write a number, 0 will stop the loop.")
    negative = 0
    even = 0

    while True:
        number = int(input())
        if is_even(number) == "even":
            even += 1

        if number == 0:
            print("Amount of negative inputs: ", negative)
            print("Amount of even numbers: ", even)
            return
        elif number < 0:
            negative += 1
            print(number)
        else:
            print(number)


ask_user()

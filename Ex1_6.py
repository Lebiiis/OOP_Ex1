# File: Ex1_6
# Author: Niki Leppänen
# Description:  Add to the previous task a function that counts the sum of the positive integers divisible by three.

def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return


def pos_div_by_three(num):
    if num > 0 and num % 3 == 0:
        return "posdivthree"
    else:
        return


def ask_user():
    print("Write a number, 0 will stop the loop.")
    negative = 0
    even = 0
    posdivthree = 0
    while True:
        number = int(input())
        if is_even(number) == "even":
            even += 1
        elif pos_div_by_three(number) == "posdivthree":
            posdivthree += 1

        if number == 0:
            print("Amount of negative inputs: ", negative)
            print("Amount of even numbers: ", even)
            print("Amount of positive integers divisible by 3: ", posdivthree)
            return
        elif number < 0:
            negative += 1
            print(number)
        else:
            print(number)


ask_user()
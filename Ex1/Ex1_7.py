# File: Ex1_7
# Author: Niki Leppänen
# Description:  Process with an arithmetic progression (AP) 2, 4, 6, ... . The maximum value of the AP is obtained from
#               the user. Countthe number of terms that appeared in the AP,
#               the sum of the terms and the sum of the squaredterms. Use functions in your solution.

# Ask user the max value of AP, store starting numbers into variables

maxval = int(input("Max value? "))

a1 = 2
a2 = 4


# Formula for arithmetic progression
def formula(a, b, max):

    numofterms = 2
    sumofterms = 0

    while True:
        c = a + b
        if c > max:
            print("Number of terms: ", numofterms)
            print("Sum of terms: ", sumofterms)
            return
        elif c == max:
            numofterms += 1
            print("Number of terms: ", numofterms)
            print("Sum of terms: ", c)
            return
        else:
            numofterms += 1
            sumofterms = a + b
            if a < b:
                a = c
            else:
                b = c


formula(a1, a2, maxval)
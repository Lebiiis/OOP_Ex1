# File: Ex1_3
# Author: Niki Leppänen
# Description:  Arrange numbers in the list from smallest to largest and strings in alphabetical order
#               and print out the lists.

# Necessary imports

import random

numlst = []
for i in range(10):
    num = int(input("Choose a number: "))
    numlst.append(num)

strlst = []
for i in range(10):
    string = input("Write something: ")
    strlst.append(string)

print(numlst)
print(strlst)

for i in range(len(numlst)-1):
    numlst[i] = random.randint(0, 9999)

print(numlst)

numlst.sort()
strlst.sort()

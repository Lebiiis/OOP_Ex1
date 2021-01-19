# File: Ex1_2
# Author: Niki Leppänen
# Description:  Code a list of at least 10 items and fill it with numbers asked from user. Do the same with strings.
#               Print out both lists.Then fill the number list with randomly generated numbers and print it out

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
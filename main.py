import random

"""Task 1"""
print("hello")

"""Task 2"""

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

"""Task 3"""

numlst.sort()
strlst.sort()

print("Sorted number list: ", numlst)
print("String list in alphabetical order: ", strlst)

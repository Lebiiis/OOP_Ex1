# File: Ex2_5
# Author: Niki Leppänen
# Description:  After writing the pseudocode, code task 4.Simple code is enough, no objects needed.

students = []
sumofgrades = 0
amountofgrades = 0

while True:
    studentname = input("\nInput your First name and Last name.\nIf you want to get the average of grades, type END.\n")
    if studentname == "END":
        break
    elif studentname not in students:
        students.append(studentname)
        grade = int(input("\nWhat was your grade?\n"))
        sumofgrades += grade
        amountofgrades += 1
    elif studentname in students:
        print("Student is already in the list.\n")

print("\nAverage of grades: ", sumofgrades / amountofgrades)




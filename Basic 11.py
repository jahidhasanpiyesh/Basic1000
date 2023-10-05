"""
Conditions  >>>Check Whether a Number is a Prime or Not in Python

Given an integer input the objective is to write a program to Check Whether a
Number is a Prime or Not in Python Language.

Input       >>> 11

Output      >>> 11 is a Prime
"""
number = int(input("Enter The any int type value:"))
for i in range(2 , number):  # range set start to end point
    # I use to three conditions if-if-else !
    if number % i == 0:
        print("Not a prime")
        break  # break use why ? jodi one conditions is true hoi then stop this code !
    if number == 2:
        print("Prime")
else:  # for loop take total conditions is False hoi then else conditions kaj start !
    print("Prime")

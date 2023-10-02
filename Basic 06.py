"""
Conditions  >>> Python Program to Check Whether a Number is Even or Odd try to problem-solve ?

Given an integer input num, the objective is to write a code to Check Whether a Number is Even or Odd in Python.
To do so we check if the number is divisible by 2 or not, it’s Even if it’s divisible otherwise Odd.

Input       >>> Any int type data/value/number

Output      >>> just show input number and number is odd/even simple !
"""
# create a variable and stor this input int type number/values !
number = int(input("Enter The Any int Number:"))
# use to three conditions  if-elif-else
if number % 2 == 0:
    print(number , "Is Even Number")
elif number == 0:
    print(number , "Is Zero")
else:
    print(number , "Is Odd Number")

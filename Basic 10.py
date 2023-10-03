"""
Conditions  >>>Check if a Year is a Leap Year or Not in Python

Given an integer input year, the objective of the code is to Check if a Year is a Leap Year or Not in Python Language.
To do so  we’ll check if the year input satisfies either of the two conditions of leap year.

Input       >>> 2020

Output      >>> It's a Leap Year.
"""

year = int(input("Enter The Any Year :"))
if year % 4 == 0 :
    print("leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("leap year")
else:
    print("not a leap year")
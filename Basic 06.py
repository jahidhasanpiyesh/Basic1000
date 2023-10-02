"""
Conditions  >>> Python Program to Check Whether a Number is Even or Odd try to problem-solve ?

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

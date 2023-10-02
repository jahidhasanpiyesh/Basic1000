"""
conditions  >>>>>: Python Program to check if a Number Is Positive Or Negative try this problem is solved ?

Given an integer input, The objective is to write a code to Check if a Number is Positive or Negative in C Language.

input >>> any number just int type data

output >>> just input number and show number is positive or negative !
"""
# just create a one variable
number = int(input("Enter the any Number :"))
# use to three conditions if-elif-else
if number >= 1:  # number is big to 1       45 56 566 its positive number
    print(number , " Is Positive Number")
elif number == 0:  # number is equal to 0
    print(number , "Is Zero")
else:  # number is small to 1            -56 -9969 -1 -2 its negative number
    print(number , "Is Negative Number")

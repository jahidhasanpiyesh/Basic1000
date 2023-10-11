"""
Conditions  >>> Check Whether the Number is a Palindrome in Python

Given an integer number as an input, the objective is to check Whether the number is a palindrome or not palindrome.
Therefore, we write a code to Check Whether the Number is a Palindrome or not palindrome in Python Language.

Input       >>>  1221

Output      >>>  Palindrome
"""
data = input()
total_data = data[::-1]  # just apply to slicing
if data == total_data:
    print("palindrome")
else:
    print('not a palindrome')


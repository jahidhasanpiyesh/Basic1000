"""
Conditions  >>> Find the sum of the Digits of a Number in Python

Given an input the objective to find the Sum of Digits of a Number in Python. To do so we’ll first extract the
last element of the number and then keep shortening the number itself.

Input       >>> 123

Output      >>> 6
"""

num = input("Enter The any value :")
data = 0  # storage data
for i in num:  # use to one loop run three time >>>>
    data = data + int(i)
print("ans is:" , data)

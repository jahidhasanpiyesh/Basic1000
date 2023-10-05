"""
Conditions  >>> Find the Prime Numbers in a Given Range in Python
Given two integer as Limits, low and high, the objective is to write a code to in Python Find Prime
Numbers in a Given Range in Python Language. To do so we’ll use nested loops to check for the Prime
while Iterating through the range.

Input       >>> low = 2 , high = 10

Output      >>> 2 3 5 7
"""
low = int(input('Enter The Any Value:'))
high = int(input('Enter The Any Value:'))
for num in range(low , high):
    if num > 1:
        for i in range(2 , num + 1):
            if num % i == 0:
                break
        else:
            print(num)

"""
Conditions  >>> Find the Sum of Numbers in a given Range in Python ?

Given two integer inputs as the range [ low , high ], the objective is to find the sum of the numbers that
lay in the intervals given by the integer inputs. Therefore, we’ll write a code to Find the Sum of the Numbers
in a Given Range in Python Language.

Input       >>> 2 5    explain >>>>> 2+3+4+5

Output      >>> 14
"""

num = 0
num1 , num2 = input(
    "Enter the two int type value : ").split()  # input data different value simple use to split()--function
print("input data dev len")
for i in range(int(num1) , int(num2) + 1):
    num += i
    print(i)  # data len print out to i . not a num variable ?
print("sum of number: " , num)

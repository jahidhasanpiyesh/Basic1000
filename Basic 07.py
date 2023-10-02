"""
Conditions  >>> Python Program to Find the Sum of First N Natural Numbers thy this problem solve ?

Input       >>> num = 8

Output      >>> 36   explain > 8 =  0, 1, 2, 3, 4, 5, 6, 7, 8
Sum of numbers = 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
"""

num = int(input("Enter The Any Int Type Value/Number :"))
total = 0  # start the number of zero
print("len of numbers 0 to" , num)  # just first positions massage show !
# using to for loop increment +1 just
for i in range(num + 1):
    total += i  # total = i+i not i+1 ok
    print(i)  # show total index data and step by step
print("Sum of number is :" , total)

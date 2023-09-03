"""
Task----------:
Write a Python program that calculates the area of a
circle based on the radius entered by the user.

Sample Output :--------
r = 1.1
Area = 3.8013271108436504
"""

# just import to math and pi
from math import pi
# enter the float type input number !
r = float(input("Enter radius number:"))
# (use to \n=newline) and (f"{}"= f-string) and (pi=total value)
# (area of a circle = pi*r**2)  (so r = radius)
print(f"r = 1.1\nArea = {pi*r**2}")  #


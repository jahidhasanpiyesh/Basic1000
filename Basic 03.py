"""
Task-------:

Write a Python program to display the current date and time.


Sample Output--------:

Current date and time :
2014-07-05 14:34:14
"""

# import datetime
import datetime
# call now() function
n = datetime.datetime.now()
print("Real device date and time")
# use to \n = new ---line--- and f"{}"= f string
print(f"{n:Date: %d-%m-%y \nTime: %H:%M:%S}")

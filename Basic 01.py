"""
Task -----------:

1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so
high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are


Output format -------:

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""
# First way this problem solve !
# simple use to right format to output and all data call just string
print("""Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are""")


# Second way this problem solve !
# use to \n = new line and \t = new tab just program call
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a "
      "diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

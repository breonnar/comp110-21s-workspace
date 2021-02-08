"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730327440"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint



score = randint(1, 100)  
print(score)


print("Your fortune cookie says...")
if score <= 13 :
    print("You will be able to buy as much boba you want without any consequences.")
if score >= 75 :
    print("Your life will be full of happiness and love.")
else:
    if score == 45 :
        print("You have a great deal of success in your future.")
    if score >= 23 or score == 44  :
        print("Don’t let your limitations overshadow your talents.")
print("Now, go spread positive vibes!")

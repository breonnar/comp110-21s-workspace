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

print(randint(1,100))


score: int = int(input("Pick a number between 0-100: "))


print("Your fortune cookie says...")
if score < 45 :
    print("You will be able to buy as much boba you want without any consequences.")
if score >= 75 :
    print("Your life will be full of happiness and love.")
else:
    if score >=45 :
        print("You have a great deal of success in your future.")
print("Now, go spread positive vibes!")

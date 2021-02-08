"""An exercise in remainders and boolean logic."""

__author__ = "730327440"

x = int(input("Pick a number between 0-100: "))

if x % 2 == 0 and x % 7 == 0:
         print("TAR HEELS")

else:
    if x % 2 == 0:
          print("TAR")

    if x % 7 == 0:
         print("HEELS")

    if x % 2 != 0 and x % 7 != 0:
        print("CAROLINA")

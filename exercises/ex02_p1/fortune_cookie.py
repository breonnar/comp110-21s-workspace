"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730327440"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: 
score = randint(1, 100) 
def fortune_cookie() -> str: 
    """Returns a random fortune."""
    if score <= 13:
        return("You will be able to buy as much boba you want without any consequences.")
    else:
        return("Your life will be full of happiness and love.")
    return str(score) 



# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()

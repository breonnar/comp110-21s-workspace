"""EX03 - palindromify function."""

__author__: str = "730327440"


def palindromify(word: str, b: bool) -> str:
    """I need to flip characters."""
    result: str = word
    if b == True: 
        # flip all characters
        for i in reversed(range(len(word))):
            result = result + word[i]  
    else:
        for i in reversed(range(len(word) - 1)):
            result = result + word[i]  
    return result
            

def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    palindromify("noon", True)
    print(palindromify("race", False))


if __name__ == "__main__":
    main()
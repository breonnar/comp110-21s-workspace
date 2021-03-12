"""EX03 - avoid_fifth function."""

__author__: str = "730327440"


def avoid_fifth(word: str) -> str:
    """Whenever strings have E or e, produce a new string them."""
    new_str: str = "" 
    i: int = 0
    while i < len(word):
        if word[i] != "E" and word[i] != "e" :
            new_str = new_str + word[i]
        i += 1
    return new_str

def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    avoid_fifth("str")
    print(avoid_fifth("HELLO, my dear friend"))


if __name__ == "__main__":
    main()
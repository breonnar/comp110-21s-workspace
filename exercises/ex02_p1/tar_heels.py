"""Tar Heels exercise redux as a structured program."""

__author__ = "730327440"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(a: int) -> str:
    """Return specific responses when divisble by certain number(s)."""
    if a % 2 == 0 and a % 7 == 0:
        return "TAR HEELS"
    else:
        if a % 2 == 0:
            return "TAR"
        if a % 7 == 0:
            return "HEELS"
        if a % 2 != 0 and a % 7 != 0:
            return "CAROLINA"





if __name__ == "__main__":
    main()

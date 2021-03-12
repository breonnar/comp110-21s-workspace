"""EX03 - prime functions."""


__author__: str = "730327440"


def is_primes(n: int) -> bool:
    """Figuring out if a number is prime or not.""" 
    i: int = 2
    while i < n:
        if (n % i) == 0:
            return False
        i = i + 1
    return True


def list_primes(a: int, b: int) -> list[int]:
    """The list for primes."""
    plist: list[int] = []
    for x in range(a,b):
        if is_primes(x):
            plist.append(x)
    return plist

def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    is_primes(2)
    print(is_primes(16))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


if __name__ == "__main__":
    main()
    is_primes(1)
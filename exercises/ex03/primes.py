"""EX03 - prime functions."""

__author__: str = "730327440"

def is_prime(n: int) -> bool:
    """Figuring out if a number is prime or not""" 
    i: int = 2
    while n >= 1:
        if (n % i) == 0:
            return False
        else:
            return True
        i=+1
    return False

    


        










def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    is_prime(1)
    print(is_prime(16))

if __name__ == "__main__":
    main()
"""EX03 - prime functions."""

__author__: str = "730327440"

def its_prime(n: int) -> bool:
    """Figuring out if a number is prime or not""" 
    i: int = 2
    while n > 1:
        if (n % i) == 0:
            return False
        elif (n % i) != 0:
            return True
        i=+1
    return False
    


        










def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    its_prime(1)
    print(its_prime(4))

if __name__ == "__main__":
    main()
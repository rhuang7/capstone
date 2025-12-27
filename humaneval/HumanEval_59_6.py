

METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29




def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Handle the case of even numbers
    while n % 2 == 0:
        n //= 2
    # Check for odd factors starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 2
    # If n is a prime number greater than 2, it is the largest prime factor
    return n

import doctest
doctest.testmod()

check(largest_prime_factor)
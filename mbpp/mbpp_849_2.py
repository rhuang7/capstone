def check(candidate):
    assert candidate(60) == 10
    assert candidate(39) == 16
    assert candidate(40) == 7


def sum_of_prime_divisors(n):
    if n < 2:
        return 0
    sum_primes = 0
    # Check for divisibility by 2
    if n % 2 == 0:
        sum_primes += 2
        while n % 2 == 0:
            n //= 2
    # Check for odd divisors from 3 upwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            sum_primes += i
            n //= i
        i += 2
    # If remaining n is a prime greater than 2
    if n > 1:
        sum_primes += n
    return sum_primes

check(sum_of_prime_divisors)
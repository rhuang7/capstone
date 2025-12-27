def check(candidate):
    assert candidate(15) == 5
    assert candidate(6) == 3
    assert candidate(2) == 2


def largest_prime_factor(n):
    if n <= 1:
        return n
    while n % 2 == 0:
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 2
    return n

check(largest_prime_factor)
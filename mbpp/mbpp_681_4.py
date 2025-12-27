def check(candidate):
    assert candidate(10) == 2
    assert candidate(25) == 5
    assert candidate(31) == 31


def smallest_prime_divisor(n):
    if n <= 1:
        return None
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

check(smallest_prime_divisor)
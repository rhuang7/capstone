def check(candidate):
    assert candidate(2) == False
    assert candidate(10) == True
    assert candidate(35) == True


def is_non_prime(n):
    if n <= 1:
        return True
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

def find_non_primes(limit):
    return [num for num in range(2, limit + 1) if is_non_prime(num)]

check(find_non_primes)
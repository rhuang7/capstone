def check(candidate):
    assert candidate(5) == 2
    assert candidate(10) == 4
    assert candidate(100) == 25


def count_primes_less_than(n):
    if n <= 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)

check(count_primes_less_than)
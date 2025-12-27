def check(candidate):
    assert candidate(6,12) == 2
    assert candidate(9,13) == 1.44
    assert candidate(1,4) == 4


def sum_of_inverse_divisors(n):
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += 1 / i
    return total

check(sum_of_inverse_divisors)
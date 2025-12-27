def check(candidate):
    assert candidate(12) == 7
    assert candidate(105) == 15
    assert candidate(2) == 2


def min_sum_of_factors(n):
    if n <= 0:
        return 0  # or raise an error, but per requirements, return 0 for non-positive n
    
    min_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            min_sum += i + n // i
    return min_sum

check(min_sum_of_factors)
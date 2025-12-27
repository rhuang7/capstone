def check(candidate):
    assert candidate(18) == 26
    assert candidate(30) == 48
    assert candidate(6) == 8


def sum_of_even_factors(n):
    if n < 1:
        return 0
    sum_even = 0
    for i in range(2, n + 1, 2):
        if n % i == 0:
            sum_even += i
    return sum_even

check(sum_of_even_factors)
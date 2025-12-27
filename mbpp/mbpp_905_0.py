def check(candidate):
    assert candidate(4) == 70
    assert candidate(5) == 252
    assert candidate(2) == 6


def sum_of_squares_of_binomial_coefficients(n):
    from math import comb
    
    total = 0
    for k in range(n + 1):
        total += comb(n, k) ** 2
    return total

check(sum_of_squares_of_binomial_coefficients)
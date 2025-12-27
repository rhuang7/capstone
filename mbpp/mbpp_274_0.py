def check(candidate):
    assert candidate(4) == 8
    assert candidate(6) == 32
    assert candidate(2) == 2


def sum_even_index_binomial_coefficients(n):
    from math import comb
    return sum(comb(n, i) for i in range(0, n+1, 2))

check(sum_even_index_binomial_coefficients)
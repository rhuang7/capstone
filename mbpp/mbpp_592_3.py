def check(candidate):
    assert candidate(3) == 15
    assert candidate(4) == 56
    assert candidate(1) == 1


def sum_product_binomial_coefficients(n):
    from math import comb
    
    total = 0
    for i in range(n + 1):
        for j in range(i + 1):
            total += comb(i, j) * comb(n - i, j)
    return total

check(sum_product_binomial_coefficients)
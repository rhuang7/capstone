def check(candidate):
    assert candidate(2) == 1056
    assert candidate(3) == 8832
    assert candidate(1) == 32


def sum_fifth_powers_even_natural(n):
    return sum(i**5 for i in range(2, 2*n+1, 2))

check(sum_fifth_powers_even_natural)
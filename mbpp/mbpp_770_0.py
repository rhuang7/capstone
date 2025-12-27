def check(candidate):
    assert candidate(2) == 82
    assert candidate(3) == 707
    assert candidate(4) == 3108


def sum_of_fourth_powers_of_odd_naturals(n):
    return sum(i**4 for i in range(1, 2*n, 2))

check(sum_of_fourth_powers_of_odd_naturals)
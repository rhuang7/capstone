def check(candidate):
    assert candidate(1) == 1
    assert candidate(2) == 244
    assert candidate(3) == 3369


def sum_of_fifth_powers_of_odd_naturals(n):
    return sum(i**5 for i in range(1, 2*n, 2))

check(sum_of_fifth_powers_of_odd_naturals)
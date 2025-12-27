def check(candidate):
    assert candidate(2) == 10
    assert candidate(3) == 35
    assert candidate(4) == 84


def sum_of_squares_of_odd_naturals(n):
    return sum(i**2 for i in range(1, 2*n, 2))

check(sum_of_squares_of_odd_naturals)
def check(candidate):
    assert candidate(2) == 20
    assert candidate(3) == 56
    assert candidate(4) == 120


def sum_of_squares_of_even_natural_numbers(n):
    return sum(i**2 for i in range(2, 2 * n + 1, 2))

check(sum_of_squares_of_even_natural_numbers)
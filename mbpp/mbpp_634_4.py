def check(candidate):
    assert candidate(2) == 272
    assert candidate(3) == 1568
    assert candidate(4) == 5664


def sum_of_fourth_powers_of_even_natural_numbers(n):
    return sum(i**4 for i in range(2, 2 * n + 1, 2))

check(sum_of_fourth_powers_of_even_natural_numbers)
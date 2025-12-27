def check(candidate):
    assert candidate(2) == 28
    assert candidate(3) == 153
    assert candidate(4) == 496


def cube_sum_of_first_n_odd_numbers(n):
    return n * (n + 1) ** 2

check(cube_sum_of_first_n_odd_numbers)
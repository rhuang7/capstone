def check(candidate):
    assert candidate(2) == 72
    assert candidate(3) == 288
    assert candidate(4) == 800


def cube_sum_first_n_even_numbers(n):
    return sum((i * 2) ** 3 for i in range(1, n + 1))

check(cube_sum_first_n_even_numbers)
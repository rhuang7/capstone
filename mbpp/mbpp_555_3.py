def check(candidate):
    assert candidate(3) == 30
    assert candidate(5) == 210
    assert candidate(2) == 6


def difference_of_cubes_and_sum(n):
    sum_of_cubes = sum(i**3 for i in range(1, n + 1))
    sum_of_numbers = sum(range(1, n + 1))
    return sum_of_cubes - sum_of_numbers

check(difference_of_cubes_and_sum)
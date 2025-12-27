def check(candidate):
    assert candidate(7)==784
    assert candidate(5)==225
    assert candidate(15)==14400


def sum_of_cubes(n):
    return sum(i**3 for i in range(1, n + 1))

check(sum_of_cubes)
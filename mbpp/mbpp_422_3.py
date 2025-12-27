def check(candidate):
    assert candidate(2) == 4.5
    assert candidate(3) == 12
    assert candidate(1) == 1


def average_of_cubes(n):
    if n <= 0:
        return 0
    total = sum(i**3 for i in range(1, n + 1))
    return total / n

check(average_of_cubes)
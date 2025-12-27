def check(candidate):
    assert candidate(5) == 225
    assert candidate(2) == 9
    assert candidate(3) == 36


def cube_sum(n):
    return sum(i**3 for i in range(1, n + 1))

check(cube_sum)
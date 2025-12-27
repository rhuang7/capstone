def check(candidate):
    assert candidate(10) == 271
    assert candidate(2) == 7
    assert candidate(9) == 217


def centered_hexagonal(n):
    return 3 * n * (n - 1) + 1

check(centered_hexagonal)
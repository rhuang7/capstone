def check(candidate):
    assert candidate(5) == 35.0
    assert candidate(6) == 56.0
    assert candidate(7) == 84.0


def nth_tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6

check(nth_tetrahedral_number)
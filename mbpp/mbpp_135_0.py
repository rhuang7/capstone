def check(candidate):
    assert candidate(10) == 190
    assert candidate(5) == 45
    assert candidate(7) == 91


def nth_hexagonal_number(n):
    return n * (2 * n - 1)

check(nth_hexagonal_number)
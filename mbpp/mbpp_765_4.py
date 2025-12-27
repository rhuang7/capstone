def check(candidate):
    assert candidate(7) == 11
    assert candidate(4) == 7
    assert candidate(9) == 13


def nth_polite_number(n):
    return n + (n * (n - 1)) // 2

check(nth_polite_number)
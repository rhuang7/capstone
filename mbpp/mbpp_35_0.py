def check(candidate):
    assert candidate(4) == 20
    assert candidate(5) == 30
    assert candidate(6) == 42


def nth_rectangular_number(n):
    return n * (n + 1) // 2

check(nth_rectangular_number)
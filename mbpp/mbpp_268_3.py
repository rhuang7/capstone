def check(candidate):
    assert candidate(3) == 37
    assert candidate(4) == 73
    assert candidate(5) == 121


def nth_star_number(n):
    return n * (3 * n - 1) // 2

check(nth_star_number)
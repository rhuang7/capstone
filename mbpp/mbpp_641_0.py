def check(candidate):
    assert candidate(10) == 325
    assert candidate(15) == 750
    assert candidate(18) == 1089


def nth_nonagonal_number(n):
    return n * (7 * n - 6) // 2

check(nth_nonagonal_number)
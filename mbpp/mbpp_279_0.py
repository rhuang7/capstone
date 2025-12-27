def check(candidate):
    assert candidate(3) == 27
    assert candidate(7) == 175
    assert candidate(10) == 370


def decagonal_number(n):
    return n * (3 * n - 2)

check(decagonal_number)
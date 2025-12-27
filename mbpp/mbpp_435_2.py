def check(candidate):
    assert candidate(123) == 3
    assert candidate(25) == 5
    assert candidate(30) == 0


def last_digit(n):
    return abs(n) % 10

check(last_digit)
def check(candidate):
    assert candidate(123) == 1
    assert candidate(456) == 4
    assert candidate(12) == 1


def first_digit(n):
    while n > 0:
        return n % 10
    return 0

check(first_digit)
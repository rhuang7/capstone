def check(candidate):
    assert candidate(9) == 76
    assert candidate(4) == 7
    assert candidate(3) == 4


def lucas_number(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

check(lucas_number)
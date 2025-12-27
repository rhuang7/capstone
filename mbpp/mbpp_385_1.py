def check(candidate):
    assert candidate(9) == 12
    assert candidate(4) == 2
    assert candidate(6) == 5


def perrin(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return perrin(n - 2) + perrin(n - 3)

check(perrin)
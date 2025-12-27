def check(candidate):
    assert candidate(60) == 106
    assert candidate(10) == 12
    assert candidate(2) == 2


def f(n):
    if n == 0:
        return 0
    return max(f(n // 2) + f(n // 3) + f(n // 4) + f(n // 5), n)

check(f)
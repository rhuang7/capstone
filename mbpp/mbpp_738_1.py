def check(candidate):
    assert candidate(7) == 1.9921875
    assert candidate(4) == 1.9375
    assert candidate(8) == 1.99609375


def geometric_sum(n):
    if n <= 0:
        return 0
    return 1 / (2 ** n) + geometric_sum(n - 1)

check(geometric_sum)
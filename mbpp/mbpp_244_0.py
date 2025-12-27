def check(candidate):
    assert candidate(35) == 36
    assert candidate(6) == 9
    assert candidate(9) == 16


def next_perfect_square(n):
    import math
    root = math.isqrt(n)
    if root * root == n:
        return (root + 1) ** 2
    else:
        return (root + 1) ** 2

check(next_perfect_square)
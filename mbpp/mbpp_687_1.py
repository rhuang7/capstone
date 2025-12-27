def check(candidate):
    assert candidate(12,14) == 2
    assert candidate(13,17) == 1
    assert candidate(9, 3) == 3


def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

check(gcd)
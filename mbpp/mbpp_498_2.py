def check(candidate):
    assert candidate(12, 17) == 1
    assert candidate(4,6) == 2
    assert candidate(2,9) == 1


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

check(gcd)
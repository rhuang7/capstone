def check(candidate):
    assert candidate(4,6) == 12
    assert candidate(15,17) == 255
    assert candidate(2,6) == 6


def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

check(lcm)
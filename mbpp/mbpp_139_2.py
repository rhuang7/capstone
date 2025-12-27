def check(candidate):
    assert candidate(10)==62.830000000000005
    assert candidate(5)==31.415000000000003
    assert candidate(4)==25.132


def circumference(radius):
    import math
    return 2 * math.pi * radius

check(circumference)
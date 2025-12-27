def check(candidate):
    assert candidate(10,5)==1570.7500000000002
    assert candidate(4,5)==251.32000000000002
    assert candidate(4,10)==502.64000000000004


def cylinder_volume(radius, height):
    import math
    return math.pi * radius ** 2 * height

check(cylinder_volume)
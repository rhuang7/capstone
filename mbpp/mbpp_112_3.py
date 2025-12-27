def check(candidate):
    assert candidate(2,4) == 12
    assert candidate(1,2) == 6
    assert candidate(3,1) == 8


def cylinder_perimeter(radius):
    import math
    return 2 * math.pi * radius

check(cylinder_perimeter)
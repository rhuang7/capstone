def check(candidate):
    assert candidate(10,5)==942.45
    assert candidate(4,5)==226.18800000000002
    assert candidate(4,10)==351.848


def cylinder_surface_area(radius, height):
    import math
    return 2 * math.pi * radius * (radius + height)

check(cylinder_surface_area)
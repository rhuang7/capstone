def check(candidate):
    assert candidate(10)==314.15000000000003
    assert candidate(5)==78.53750000000001
    assert candidate(4)==50.264


def cylinder_surface_area(radius, height, top=True):
    import math
    if top:
        return 2 * math.pi * radius * (radius + height)
    else:
        return 2 * math.pi * radius * (radius + height) - 2 * math.pi * radius**2

check(cylinder_surface_area)
def check(candidate):
    assert candidate(5,12)==204.20352248333654
    assert candidate(10,15)==566.3586699569488
    assert candidate(19,17)==1521.8090132193388


def lateral_surface_area_cone(radius, slant_height):
    import math
    return math.pi * radius * slant_height

check(lateral_surface_area_cone)
def check(candidate):
    assert candidate(10,5)==314.15000000000003
    assert candidate(4,5)==125.66000000000001
    assert candidate(4,10)==251.32000000000002


def lateral_surface_area(radius, height):
    import math
    return 2 * math.pi * radius * height

check(lateral_surface_area)
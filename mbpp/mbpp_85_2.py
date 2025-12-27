def check(candidate):
    assert candidate(10)==1256.6370614359173
    assert candidate(15)==2827.4333882308138
    assert candidate(20)==5026.548245743669


def surface_area_of_sphere(radius):
    import math
    return 4 * math.pi * radius ** 2

check(surface_area_of_sphere)
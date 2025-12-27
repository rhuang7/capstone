def check(candidate):
    assert candidate(5,12)==282.7433388230814
    assert candidate(10,15)==880.5179353159282
    assert candidate(19,17)==2655.923961165254


def surface_area_of_cone(radius, slant_height):
    import math
    base_area = math.pi * radius ** 2
    lateral_area = math.pi * radius * slant_height
    return base_area + lateral_area

check(surface_area_of_cone)
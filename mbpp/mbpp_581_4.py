def check(candidate):
    assert candidate(3,4) == 33
    assert candidate(4,5) == 56
    assert candidate(1,2) == 5


def surface_area_square_pyramid(base_edge, slant_height):
    base_area = base_edge ** 2
    lateral_area = 4 * base_edge * slant_height
    return base_area + lateral_area

check(surface_area_square_pyramid)
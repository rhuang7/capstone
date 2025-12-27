def check(candidate):
    assert candidate(5)==150
    assert candidate(3)==54
    assert candidate(10)==600


def surface_area_cube(side_length):
    return 6 * side_length ** 2

check(surface_area_cube)
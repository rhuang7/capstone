def check(candidate):
    assert candidate(5)==100
    assert candidate(9)==324
    assert candidate(10)==400


def lateral_surface_area_cube(side_length):
    return 4 * side_length ** 2

check(lateral_surface_area_cube)
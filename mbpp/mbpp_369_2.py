def check(candidate):
    assert candidate(8,5,6)==156
    assert candidate(7,9,10)==320
    assert candidate(10,20,30)==1800


def lateral_surface_area(length, width, height):
    return 2 * height * (length + width)

check(lateral_surface_area)
def check(candidate):
    assert candidate(4,45)==6.285714285714286
    assert candidate(9,45)==31.82142857142857
    assert candidate(9,360)==None


def calculate_sector_area(radius, angle_degrees):
    import math
    angle_radians = math.radians(angle_degrees)
    area = 0.5 * radius ** 2 * angle_radians
    return area

check(calculate_sector_area)
def check(candidate):
    assert candidate(0) == 0
    assert candidate(-1) == -1
    assert candidate(2) == 4


def largest_triangle_in_semicircle(radius):
    import math
    
    # The largest triangle that can be inscribed in a semicircle
    # is a right-angled triangle with the hypotenuse as the diameter
    # and the right angle on the circumference.
    # The area of this triangle is (base * height) / 2
    # where base = 2 * radius (diameter), height = radius
    
    base = 2 * radius
    height = radius
    area = (base * height) / 2
    
    return area

check(largest_triangle_in_semicircle)
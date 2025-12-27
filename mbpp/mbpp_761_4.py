def check(candidate):
    assert candidate(9,45)==3.5357142857142856
    assert candidate(9,480)==None
    assert candidate(5,270)==11.785714285714285


def arc_length(radius, angle_degrees):
    import math
    angle_radians = math.radians(angle_degrees)
    return radius * angle_radians

check(arc_length)
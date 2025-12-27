def check(candidate):
    assert candidate(90)==1.5707963267948966
    assert candidate(60)==1.0471975511965976
    assert candidate(120)==2.0943951023931953


def degrees_to_radians(degrees):
    import math
    return math.radians(degrees)

check(degrees_to_radians)
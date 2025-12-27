def check(candidate):
    assert candidate(1) == (1.0, 0.0)
    assert candidate(4) == (4.0,0.0)
    assert candidate(5) == (5.0,0.0)


def complex_to_polar(complex_num):
    import math
    real = complex_num.real
    imag = complex_num.imag
    magnitude = math.hypot(real, imag)
    angle = math.atan2(imag, real)
    return magnitude, angle

check(complex_to_polar)
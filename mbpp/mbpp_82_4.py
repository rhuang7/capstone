def check(candidate):
    assert candidate(10)==4188.790204786391
    assert candidate(25)==65449.84694978735
    assert candidate(20)==33510.32163829113


def sphere_volume(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)

check(sphere_volume)
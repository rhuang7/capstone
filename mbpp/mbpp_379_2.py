def check(candidate):
    assert candidate(1,2,3)==22
    assert candidate(5,7,9)==286
    assert candidate(10,15,21)==1350


def surface_area_cuboid(length, width, height):
    return 2 * (length * width + width * height + height * length)

check(surface_area_cuboid)
def check(candidate):
    assert candidate(1,2,3)==6
    assert candidate(5,7,9)==315
    assert candidate(10,15,21)==3150


def calculate_cuboid_volume(length, width, height):
    return length * width * height

check(calculate_cuboid_volume)
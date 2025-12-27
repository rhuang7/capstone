def check(candidate):
    assert candidate(3)==27
    assert candidate(2)==8
    assert candidate(5)==125


def cube_volume(side_length):
    return side_length ** 3

check(cube_volume)
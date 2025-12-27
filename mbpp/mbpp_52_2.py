def check(candidate):
    assert candidate(10,20)==200
    assert candidate(15,20)==300
    assert candidate(8,9)==72


def calculate_parallelogram_area(base, height):
    return base * height

check(calculate_parallelogram_area)
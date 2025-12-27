def check(candidate):
    assert candidate(10,20)==200
    assert candidate(10,5)==50
    assert candidate(4,2)==8


def rectangle_area(length, width):
    return length * width

check(rectangle_area)
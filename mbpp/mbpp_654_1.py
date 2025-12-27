def check(candidate):
    assert candidate(10,20)==60
    assert candidate(10,5)==30
    assert candidate(4,2)==12


def rectangle_perimeter(length, width):
    return 2 * (length + width)

check(rectangle_perimeter)
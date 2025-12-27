def check(candidate):
    assert candidate(10,20,30)==60
    assert candidate(3,4,5)==12
    assert candidate(25,35,45)==105


def triangle_perimeter(a, b, c):
    return a + b + c

check(triangle_perimeter)
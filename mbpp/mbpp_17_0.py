def check(candidate):
    assert candidate(10)==40
    assert candidate(5)==20
    assert candidate(4)==16


def square_perimeter(side):
    return 4 * side

check(square_perimeter)
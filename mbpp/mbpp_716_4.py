def check(candidate):
    assert candidate(10)==40
    assert candidate(5)==20
    assert candidate(4)==16


def find_rhombus_perimeter(side_length):
    return 4 * side_length

check(find_rhombus_perimeter)
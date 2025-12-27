def check(candidate):
    assert candidate(5)==25
    assert candidate(10)==50
    assert candidate(15)==75


def calculate_pentagon_perimeter(side_length):
    return 5 * side_length

check(calculate_pentagon_perimeter)
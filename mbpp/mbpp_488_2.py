def check(candidate):
    assert candidate(5)==43.01193501472417
    assert candidate(10)==172.0477400588967
    assert candidate(15)==387.10741513251753


def calculate_pentagon_area(side_length):
    import math
    # Formula for area of a regular pentagon: (5 * side^2) / (4 * tan(π/5))
    return (5 * side_length ** 2) / (4 * math.tan(math.pi / 5))

check(calculate_pentagon_area)
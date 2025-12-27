def check(candidate):
    assert candidate(4,20)==80
    assert candidate(10,15)==150
    assert candidate(9,7)==63


def calculate_regular_polygon_perimeter(side_length, num_sides):
    return side_length * num_sides

check(calculate_regular_polygon_perimeter)
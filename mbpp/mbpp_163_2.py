def check(candidate):
    assert candidate(4,20)==400.00000000000006
    assert candidate(10,15)==1731.1969896610804
    assert candidate(9,7)==302.90938549487214


def calculate_polygon_area(sides, side_length):
    import math
    # Formula for the area of a regular polygon: (perimeter * apothem) / 2
    # Apothem = (side_length) / (2 * tan(π / sides))
    perimeter = sides * side_length
    apothem = side_length / (2 * math.tan(math.pi / sides))
    area = (perimeter * apothem) / 2
    return area

check(calculate_polygon_area)
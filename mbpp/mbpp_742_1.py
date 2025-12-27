def check(candidate):
    assert candidate(3)==15.588457268119894
    assert candidate(20)==692.8203230275509
    assert candidate(10)==173.20508075688772


def calculate_tetrahedron_area(edge_length):
    import math
    # Area of a tetrahedron = sqrt(3) * (edge_length ** 2)
    return math.sqrt(3) * (edge_length ** 2)

check(calculate_tetrahedron_area)
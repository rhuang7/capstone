def check(candidate):
    assert candidate(10)==117.85
    assert candidate(15)==397.75
    assert candidate(20)==942.81


def tetrahedron_volume(edge_length):
    return (edge_length ** 3) / (6 * 6)

check(tetrahedron_volume)
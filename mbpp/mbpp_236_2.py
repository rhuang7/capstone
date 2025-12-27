def check(candidate):
    assert candidate(4,2) == 7
    assert candidate(4,3) == 3
    assert candidate(1,3) == -1


def count_equilateral_triangles(n):
    """
    Count the maximum number of equilateral triangles that can be formed
    within a given equilateral triangle of side length n.
    """
    return (n * (n + 1) * (2 * n + 1)) // 6

check(count_equilateral_triangles)
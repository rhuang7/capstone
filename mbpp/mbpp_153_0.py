def check(candidate):
    assert candidate(5,3,2)==(-0.3, 1.55)
    assert candidate(9,8,4)==(-0.4444444444444444, 2.2222222222222223)
    assert candidate(2,4,6)==(-1.0, 4.0)


def find_parabola_vertex(a, b, c):
    """
    Calculate the vertex of a parabola given in standard form ax^2 + bx + c.
    The vertex is at (-b/(2a), f(-b/(2a))).
    """
    x = -b / (2 * a)
    y = a * x**2 + b * x + c
    return (x, y)

check(find_parabola_vertex)
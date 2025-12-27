def check(candidate):
    assert candidate(5,3,2)==(-0.3, 1.6)
    assert candidate(9,8,4)==(-0.4444444444444444, 2.25)
    assert candidate(2,4,6)==(-1.0, 4.125)


def find_parabola_focus(a, b, c):
    """
    Calculate the focus of a parabola given in standard form ax^2 + bx + c = 0.
    The focus is located at (h, k + 1/(4a)), where (h, k) is the vertex of the parabola.
    """
    # Calculate the vertex (h, k)
    h = -b / (2 * a)
    k = (4 * a * c - b ** 2) / (4 * a)
    
    # Calculate the focus
    focus_x = h
    focus_y = k + 1 / (4 * a)
    
    return (focus_x, focus_y)

check(find_parabola_focus)
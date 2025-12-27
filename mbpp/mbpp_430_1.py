def check(candidate):
    assert candidate(5,3,2)==-198
    assert candidate(9,8,4)==-2336
    assert candidate(2,4,6)==-130


def find_directrix(a):
    """
    Returns the equation of the directrix of a parabola in the form y = k.
    Assumes the parabola is in the standard form y = ax^2 + bx + c.
    The directrix is calculated based on the vertex form of the parabola.
    """
    # For a parabola in the form y = a(x - h)^2 + k, the directrix is y = -1/(4a) + k
    # Since the function is given 'a' as the coefficient, we assume the vertex is at (0, 0)
    # So the directrix is y = -1/(4a)
    return -1/(4 * a)

check(find_directrix)
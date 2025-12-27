def check(candidate):
    assert candidate((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))
    assert candidate((1, 2), 3) == ((1, 2), (1, 2), (1, 2))
    assert candidate((3, 4), 5) == ((3, 4), (3, 4), (3, 4), (3, 4), (3, 4))


def repeat_tuple(t, n):
    return t * n

check(repeat_tuple)
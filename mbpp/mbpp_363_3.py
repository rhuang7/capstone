def check(candidate):
    assert candidate([(1, 3, 4), (2, 4, 6), (3, 8, 1)], 4) == [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
    assert candidate([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 8) == [(9, 10, 11), (12, 13, 14), (15, 16, 17)]
    assert candidate([(11, 12, 13), (14, 15, 16), (17, 18, 19)], 9) == [(20, 21, 22), (23, 24, 25), (26, 27, 28)]


def add_to_tuple_elements(t, k):
    return tuple(x + k for x in t)

check(add_to_tuple_elements)
def check(candidate):
    assert candidate("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)
    assert candidate("1, 2, 3, 4, 5") == (1, 2, 3, 4, 5)
    assert candidate("4, 6, 9, 11, 13, 14") == (4, 6, 9, 11, 13, 14)


def string_to_tuple(s):
    return tuple(map(int, s.split()))

check(string_to_tuple)
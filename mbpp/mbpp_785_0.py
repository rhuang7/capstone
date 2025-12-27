def check(candidate):
    assert candidate("(7, 8, 9)") == (7, 8, 9)
    assert candidate("(1, 2, 3)") == (1, 2, 3)
    assert candidate("(4, 5, 6)") == (4, 5, 6)


def tuple_string_to_integer_tuple(s):
    return tuple(map(int, s.split()))

check(tuple_string_to_integer_tuple)
def check(candidate):
    assert candidate("1.2, 1.3, 2.3, 2.4, 6.5") == (1.2, 1.3, 2.3, 2.4, 6.5)
    assert candidate("2.3, 2.4, 5.6, 5.4, 8.9") == (2.3, 2.4, 5.6, 5.4, 8.9)
    assert candidate("0.3, 0.5, 7.8, 9.4") == (0.3, 0.5, 7.8, 9.4)


def string_to_tuple(s):
    return tuple(map(float, s.split()))

check(string_to_tuple)
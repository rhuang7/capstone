def check(candidate):
    assert candidate((4, 56)) == 4.56
    assert candidate((7, 256)) == 7.256
    assert candidate((8, 123)) == 8.123


def tuple_to_float(t):
    return float(t[0])

check(tuple_to_float)
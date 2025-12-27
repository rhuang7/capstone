def check(candidate):
    assert candidate((10, 4, 5, 6, None)) == True
    assert candidate((7, 8, 9, 11, 14)) == False
    assert candidate((1, 2, 3, 4, None)) == True


def has_none_value(tup):
    return None in tup

check(has_none_value)
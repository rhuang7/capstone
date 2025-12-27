def check(candidate):
    assert candidate((1, 3, 5, 2, 3, 5, 1, 1, 3)) == (1, 2, 3, 5)
    assert candidate((2, 3, 4, 4, 5, 6, 6, 7, 8, 8)) == (2, 3, 4, 5, 6, 7, 8)
    assert candidate((11, 12, 13, 11, 11, 12, 14, 13)) == (11, 12, 13, 14)


def remove_duplicates(input_tuple):
    return tuple(set(input_tuple))

check(remove_duplicates)
def check(candidate):
    assert candidate({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
    assert candidate({6, 7, 8, 9, 10, 11}) == (6, 7, 8, 9, 10, 11)
    assert candidate({12, 13, 14, 15, 16}) == (12, 13, 14, 15, 16)


def set_to_ordered_tuples(input_set):
    return tuple(sorted(input_set))

check(set_to_ordered_tuples)
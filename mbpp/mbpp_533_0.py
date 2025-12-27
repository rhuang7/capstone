def check(candidate):
    assert candidate((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]
    assert candidate((7, 8, 9, "SR"), str) == [7, 8, 9]
    assert candidate((7, 1.1, 2, 2.2), float) == [7, 2]


def remove_elements_by_type(tup, data_type):
    return tuple(x for x in tup if not isinstance(x, data_type))

check(remove_elements_by_type)
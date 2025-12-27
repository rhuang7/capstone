def check(candidate):
    assert candidate((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert candidate((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
    assert candidate((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)


def remove_nested_record(tup):
    return tuple(item for item in tup if not isinstance(item, tuple))

check(remove_nested_record)
def check(candidate):
    assert candidate((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
    assert candidate((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)
    assert candidate((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)


def union_of_tuples(t1, t2):
    return tuple(set(t1) | set(t2))

check(union_of_tuples)
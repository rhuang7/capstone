def check(candidate):
    assert candidate((3, 4), (5, 6)) == (3, 4, 5, 6)
    assert candidate((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert candidate((4, 5), (6, 8)) == (4, 5, 6, 8)


def concatenate_tuples(t1, t2):
    return (t1, t2)

check(concatenate_tuples)
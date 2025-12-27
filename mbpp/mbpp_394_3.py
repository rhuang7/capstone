def check(candidate):
    assert candidate((1, 4, 5, 6, 1, 4)) == False
    assert candidate((1, 4, 5, 6)) == True
    assert candidate((2, 3, 4, 5, 6)) == True


def is_distinct_tuple(t):
    return len(set(t)) == len(t)

check(is_distinct_tuple)
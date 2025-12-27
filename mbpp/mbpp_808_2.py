def check(candidate):
    assert candidate((10, 4, 5, 6, 8), 6) == True
    assert candidate((1, 2, 3, 4, 5, 6), 7) == False
    assert candidate((7, 8, 9, 44, 11, 12), 11) == True


def contains_k(tuples, k):
    for t in tuples:
        if k in t:
            return True
    return False

check(contains_k)
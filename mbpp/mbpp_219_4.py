def check(candidate):
    assert candidate((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)
    assert candidate((4, 5, 6, 1, 2, 7), 3) == (1, 2, 4, 5, 6, 7)
    assert candidate((2, 3, 4, 8, 9, 11, 7), 4) == (2, 3, 4, 7, 8, 9, 11)


def find_k_extremes(tup, k):
    if k <= 0:
        return None, None
    if k > len(tup):
        return None, None
    sorted_tup = sorted(tup)
    max_val = sorted_tup[-k]
    min_val = sorted_tup[k-1]
    return max_val, min_val

check(find_k_extremes)
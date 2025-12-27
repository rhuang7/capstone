def check(candidate):
    assert candidate((3, 5, 6, 5, 3, 6),[3, 6, 5]) == True
    assert candidate((4, 5, 6, 4, 6, 5),[4, 5, 6]) == True
    assert candidate((9, 8, 7, 6, 8, 9),[9, 8, 1]) == False


def has_k_elements(t, k):
    return len(t) == k

check(has_k_elements)
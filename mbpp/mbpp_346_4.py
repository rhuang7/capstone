def check(candidate):
    assert candidate(4, 3) == 5
    assert candidate(4, 2) == 4
    assert candidate(3, 1) == 1


def entringer_number(n, k):
    if k == 0 or k == n:
        return 1
    return entringer_number(n-1, k-1) + entringer_number(n-1, k)

check(entringer_number)
def check(candidate):
    assert candidate(3, 4) == 129
    assert candidate(3, 3) == 63
    assert candidate(4, 5) == 681


def delannoy_number(n, k):
    """
    Calculate the nth Delannoy number for a given k.
    """
    if n < 0 or k < 0:
        return 0
    if n == 0 or k == 0:
        return 1
    return delannoy_number(n - 1, k) + delannoy_number(n, k - 1) + delannoy_number(n - 1, k - 1)

def nth_delannoy(n, k):
    """
    Find the nth Delannoy number for a given k.
    """
    return delannoy_number(n, k)

check(nth_delannoy)
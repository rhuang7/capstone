def check(candidate):
    assert candidate(5) == 31
    assert candidate(2) == 5
    assert candidate(4) == 17


def jacobsthal_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + 2 * b
        return b

check(jacobsthal_lucas)
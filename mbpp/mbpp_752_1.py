def check(candidate):
    assert candidate(5) == 11
    assert candidate(2) == 1
    assert candidate(4) == 5


def jacobsthal(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (jacobsthal(n-1) + jacobsthal(n-2)) * 2

check(jacobsthal)
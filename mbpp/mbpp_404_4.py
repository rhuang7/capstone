def check(candidate):
    assert candidate(1,2) == 1
    assert candidate(-5,-4) == -5
    assert candidate(0,0) == 0


def find_minimum(a, b):
    return min(a, b)

check(find_minimum)
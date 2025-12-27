def check(candidate):
    assert candidate(1,-2) == True
    assert candidate(3,2) == False
    assert candidate(-10,-10) == False


def have_opposite_sign(a, b):
    return (a > 0 and b < 0) or (a < 0 and b > 0)

check(have_opposite_sign)
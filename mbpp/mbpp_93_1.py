def check(candidate):
    assert candidate(3,4) == 81
    assert candidate(2,3) == 8
    assert candidate(5,5) == 3125


def power(a, b):
    return a ** b

check(power)
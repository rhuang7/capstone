def check(candidate):
    assert candidate(123.01247,0)==124
    assert candidate(123.01247,1)==123.1
    assert candidate(123.01247,2)==123.02


def round_up(number, digits):
    import math
    return math.ceil(number * (10 ** digits)) / (10 ** digits)

check(round_up)
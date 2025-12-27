def check(candidate):
    assert candidate(2,10,11,20)==20
    assert candidate(15,17,1,10)==32
    assert candidate(10,15,5,30)==20


def add_with_range_check(a, b, lower, upper):
    total = a + b
    if lower <= total <= upper:
        return 20
    return total

check(add_with_range_check)
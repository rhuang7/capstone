def check(candidate):
    assert candidate(5)==True
    assert candidate(2)==False
    assert candidate(6)==False


def has_31_days(month):
    return month in [1, 3, 5, 7, 8, 10, 12]

check(has_31_days)
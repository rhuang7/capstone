def check(candidate):
    assert candidate(6)==True
    assert candidate(2)==False
    assert candidate(12)==False


def has_30_days(month):
    return month in [4, 6, 9, 11]

check(has_30_days)
def check(candidate):
    assert candidate(2)==True
    assert candidate(1)==False
    assert candidate(3)==False


def has_28_days(month):
    # February is the only month with 28 days (excluding leap years)
    return month == 2

check(has_28_days)
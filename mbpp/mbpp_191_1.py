def check(candidate):
    assert candidate("February")==False
    assert candidate("June")==True
    assert candidate("April")==True


def has_30_days(month_name):
    thirty_day_months = {"April", "June", "September", "November"}
    return month_name in thirty_day_months

check(has_30_days)
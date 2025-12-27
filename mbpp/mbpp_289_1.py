def check(candidate):
    assert candidate(100) == 5
    assert candidate(50) ==6
    assert candidate(75) == 2


def count_odd_days(year):
    import calendar
    return sum(1 for month in range(1, 13) if calendar.monthrange(year, month)[1] % 2 != 0)

check(count_odd_days)
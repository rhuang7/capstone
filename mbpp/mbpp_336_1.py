def check(candidate):
    assert candidate("February")==True
    assert candidate("January")==False
    assert candidate("March")==False


def has_28_days(month_name):
    # Dictionary mapping month names to their number of days
    month_days = {
        'january': 31,
        'february': 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }
    # Check if the month is in the dictionary and if it has 28 days
    return month_name.lower() in month_days and month_days[month_name.lower()] == 28

check(has_28_days)
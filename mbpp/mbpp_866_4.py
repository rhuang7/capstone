def check(candidate):
    assert candidate("February")==False
    assert candidate("January")==True
    assert candidate("March")==True


def has_31_days(month_name):
    month_days = {
        "january": 31, "february": 28, "march": 31, "april": 30,
        "may": 31, "june": 30, "july": 31, "august": 31,
        "september": 30, "october": 31, "november": 30, "december": 31
    }
    return month_days.get(month_name.lower()) == 31

check(has_31_days)
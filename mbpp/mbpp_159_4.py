def check(candidate):
    assert candidate('January',4)==('winter')
    assert candidate('October',28)==('autumn')
    assert candidate('June',6)==('spring')


def get_season(month, day):
    if (month == 12 or month == 1 or month == 2) or (month == 3 and day >= 21):
        return "Winter"
    elif (month == 3 or month == 4 or month == 5) or (month == 6 and day >= 21):
        return "Spring"
    elif (month == 6 or month == 7 or month == 8) or (month == 9 and day >= 21):
        return "Summer"
    else:
        return "Autumn"

check(get_season)
def check(candidate):
    assert candidate(11,11,2002)==True
    assert candidate(13,11,2002)==False
    assert candidate('11','11','2002')==True


def is_valid_gregorian_date(year, month, day):
    if not (1 <= year <= 9999):
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False
    
    # Days in each month (non-leap year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29
    
    if day > month_days[month - 1]:
        return False
    
    return True

check(is_valid_gregorian_date)
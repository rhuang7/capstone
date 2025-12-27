def check(candidate):
    assert candidate('123.11')==True
    assert candidate('e666.86')==False
    assert candidate('3.124587')==False


def check_decimal_with_precision(value):
    return round(value, 2)

check(check_decimal_with_precision)
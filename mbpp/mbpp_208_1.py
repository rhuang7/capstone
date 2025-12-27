def check(candidate):
    assert candidate('123.11') == True
    assert candidate('0.21') == True
    assert candidate('123.1214') == False


import re

def check_decimal_precision(value):
    pattern = r'^\d+(\.\d{2})?$'
    return bool(re.match(pattern, str(value)))

check(check_decimal_precision)
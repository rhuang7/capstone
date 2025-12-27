def check(candidate):
    assert candidate("2026-01-02") == '02-01-2026'
    assert candidate("2020-11-13") == '13-11-2020'
    assert candidate("2021-04-26") == '26-04-2021'


import re

def convert_date_format(date_str):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    replacement = r'\3-\2-\1'
    return re.sub(pattern, replacement, date_str)

check(convert_date_format)
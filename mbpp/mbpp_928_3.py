def check(candidate):
    assert candidate('2026-01-02')=='02-01-2026'
    assert candidate('2021-01-04')=='04-01-2021'
    assert candidate('2030-06-06')=='06-06-2030'


def convert_date_format(date_str):
    year, month, day = map(int, date_str.split('-'))
    return f"{day}-{month}-{year}"

check(convert_date_format)
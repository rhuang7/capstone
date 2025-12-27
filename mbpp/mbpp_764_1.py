def check(candidate):
    assert candidate('program2bedone') == 1
    assert candidate('3wonders') ==1
    assert candidate('123') == 3


def count_numeric_values(s):
    return sum(1 for char in s if char.isdigit())

check(count_numeric_values)
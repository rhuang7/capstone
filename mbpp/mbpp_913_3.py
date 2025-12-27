def check(candidate):
    assert candidate('abcdef')==False
    assert candidate('abcdef7')==True
    assert candidate('abc')==False


def ends_with_number(s):
    import re
    return bool(re.search(r'\d$', s))

check(ends_with_number)
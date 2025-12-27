def check(candidate):
    assert candidate("ac")==('Not matched!')
    assert candidate("dc")==('Not matched!')
    assert candidate("abbbba")==('Found a match!')


def match_abbbb(s):
    import re
    return bool(re.fullmatch(r'abbbb', s))

check(match_abbbb)
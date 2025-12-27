def check(candidate):
    assert candidate("ac")==('Not matched!')
    assert candidate("dc")==('Not matched!')
    assert candidate("abba")==('Found a match!')


def match_ab(s):
    import re
    pattern = r'^a[b]+$
    return bool(re.match(pattern, s))

check(b)
def check(candidate):
    assert candidate("ac")==('Found a match!')
    assert candidate("dc")==('Not matched!')
    assert candidate("abba")==('Found a match!')


def match_a_b(s):
    import re
    pattern = r'^a[b]*$'
    return bool(re.match(pattern, s))

check(match_a_b)
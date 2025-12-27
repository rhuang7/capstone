def check(candidate):
    assert candidate("ac")==('Not matched!')
    assert candidate("dc")==('Not matched!')
    assert candidate("abbbba")==('Found a match!')


def match_ab_pattern(s):
    import re
    pattern = r'^a[b]{2,3}$'
    return bool(re.match(pattern, s))

check(match_ab_pattern)
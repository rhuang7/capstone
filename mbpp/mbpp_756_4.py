def check(candidate):
    assert candidate("ac")==('Found a match!')
    assert candidate("dc")==('Not matched!')
    assert candidate("abbbba")==('Found a match!')


def match_pattern(s):
    import re
    pattern = r'^a[b]?$'
    return re.match(pattern, s) is not None

check(match_pattern)
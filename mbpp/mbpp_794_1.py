def check(candidate):
    assert candidate("aabbbb")==('Found a match!')
    assert candidate("aabAbbbc")==('Not matched!')
    assert candidate("accddbbjjj")==('Not matched!')


def match_pattern(s):
    import re
    pattern = r'^a.*b$'
    return bool(re.match(pattern, s))

check(match_pattern)
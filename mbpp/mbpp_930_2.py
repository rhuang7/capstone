def check(candidate):
    assert candidate("msb") == 'Not matched!'
    assert candidate("a0c") == 'Found a match!'
    assert candidate("abbc") == 'Found a match!'


import re

def match_a_followed_by_bs(s):
    pattern = r'^a[b]*$'
    return bool(re.match(pattern, s))

check(match_a_followed_by_bs)
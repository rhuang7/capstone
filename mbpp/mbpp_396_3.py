def check(candidate):
    assert candidate("abba") == "Valid"
    assert candidate("a") == "Valid"
    assert candidate("abcd") == "Invalid"


import re

def starts_and_ends_with_same_char(s):
    pattern = r'^(\w)\1$'
    return bool(re.match(pattern, s))

check(starts_and_ends_with_same_char)
def check(candidate):
    assert candidate("annie") == 'Valid'
    assert candidate("dawood") == 'Invalid'
    assert candidate("Else") == 'Valid'


import re

def starts_with_vowel(s):
    pattern = r'^[aeiouAEIOU]'
    return bool(re.match(pattern, s))

check(starts_with_vowel)
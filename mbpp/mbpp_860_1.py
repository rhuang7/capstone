def check(candidate):
    assert candidate("dawood@") == 'Discard'
    assert candidate("skdmsam326") == 'Accept'
    assert candidate("cooltricks@") == 'Discard'


import re

def is_ending_with_alphanumeric(s):
    pattern = r'^.*[a-zA-Z0-9]$'
    return bool(re.match(pattern, s))

check(is_ending_with_alphanumeric)
def check(candidate):
    assert candidate('Google      Assistant') == 'Google Assistant'
    assert candidate('Quad      Core') == 'Quad Core'
    assert candidate('ChromeCast      Built-in') == 'ChromeCast Built-in'


import re

def remove_multiple_spaces(s):
    return re.sub(r' +', ' ', s)

check(remove_multiple_spaces)
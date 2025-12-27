def check(candidate):
    assert candidate('The quick brown fox jumps over the lazy dog.',['fox']) == 'Matched!'
    assert candidate('The quick brown fox jumps over the lazy dog.',['horse']) == 'Not Matched!'
    assert candidate('The quick brown fox jumps over the lazy dog.',['lazy']) == 'Matched!'


import re

def search_literals_in_string(text, literals):
    matches = []
    for literal in literals:
        pattern = re.compile(re.escape(literal))
        match = pattern.search(text)
        if match:
            matches.append(match.group())
    return matches

check(search_literals_in_string)
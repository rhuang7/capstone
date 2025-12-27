def check(candidate):
    assert candidate("aabbbbd") == 'Not matched!'
    assert candidate("aabAbbbc") == 'Not matched!'
    assert candidate("accddbbjjjb") == 'Found a match!'


import re

def match_a_followed_by_anything_ending_in_b(s):
    pattern = r'^a.*b$'
    return re.match(pattern, s) is not None

check(match_a_followed_by_anything_ending_in_b)
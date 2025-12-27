def check(candidate):
    assert candidate("aab_cbbbc") == 'Found a match!'
    assert candidate("aab_Abbbc") == 'Not matched!'
    assert candidate("Aaab_abbbc") == 'Not matched!'


import re

def find_lowercase_underscore_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    matches = re.findall(pattern, text)
    return matches

check(find_lowercase_underscore_sequences)
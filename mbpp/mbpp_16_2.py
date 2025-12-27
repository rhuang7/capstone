def check(candidate):
    assert candidate("aab_cbbbc")==('Found a match!')
    assert candidate("aab_Abbbc")==('Not matched!')
    assert candidate("Aaab_abbbc")==('Not matched!')


import re

def find_lowercase_sequences(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

check(find_lowercase_sequences)
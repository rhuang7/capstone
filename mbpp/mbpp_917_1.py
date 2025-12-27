def check(candidate):
    assert candidate("AaBbGg")==('Found a match!')
    assert candidate("aA")==('Not matched!')
    assert candidate("PYTHON")==('Not matched!')


import re

def find_uppercase_sequences(text):
    return re.findall(r'[A-Z][a-z]+', text)

check(find_uppercase_sequences)
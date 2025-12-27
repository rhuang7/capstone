def check(candidate):
    assert candidate("Geeks") == 'Yes'
    assert candidate("geeksforGeeks") == 'Yes'
    assert candidate("geeks") == 'No'


import re

def find_uppercase_sequences(s):
    return re.findall(r'[A-Z][a-z]+', s)

check(find_uppercase_sequences)
def check(candidate):
    assert candidate("PYTHon")==('PYTH')
    assert candidate("FInD")==('FID')
    assert candidate("STRinG")==('STRG')


def remove_lowercase_substrings(s):
    return ''.join(char for char in s if not char.islower())

check(remove_lowercase_substrings)
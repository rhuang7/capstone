def check(candidate):
    assert candidate('aba') == False
    assert candidate('abc') == True
    assert candidate('abab') == False


def has_unique_characters(s):
    return len(set(s)) == len(s)

check(has_unique_characters)
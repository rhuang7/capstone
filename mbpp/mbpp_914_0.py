def check(candidate):
    assert candidate("abab") == True
    assert candidate("aaaa") == False
    assert candidate("xyz") == False


def is_alternating(s):
    if len(s) < 2:
        return True
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

check(is_alternating)
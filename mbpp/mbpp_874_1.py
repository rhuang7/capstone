def check(candidate):
    assert candidate("abcabcabc","abc") == True
    assert candidate("abcab","abc") == False
    assert candidate("aba","ab") == False


def is_concatenation(s, substr):
    if not s or not substr:
        return False
    if len(substr) > len(s):
        return False
    count = 0
    for i in range(0, len(s), len(substr)):
        if s[i:i+len(substr)] != substr:
            return False
        count += 1
    return True

check(is_concatenation)
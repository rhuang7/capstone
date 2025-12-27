def check(candidate):
    assert candidate("abcda") == "Equal"
    assert candidate("ab") == "Not Equal"
    assert candidate("mad") == "Not Equal"


def are_first_last_equal(s):
    if len(s) == 0:
        return False
    return s[0] == s[-1]

check(are_first_last_equal)
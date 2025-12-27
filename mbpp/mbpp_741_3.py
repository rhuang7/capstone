def check(candidate):
    assert candidate("python") == False
    assert candidate("aaa") == True
    assert candidate("data") == False


def all_characters_same(s):
    if len(s) <= 1:
        return True
    return all(c == s[0] for c in s)

check(all_characters_same)
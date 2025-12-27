def check(candidate):
    assert candidate("1212121") == True
    assert candidate("1991") == False
    assert candidate("121") == True


def is_undulating(n):
    if n < 100 or n > 999:
        return False
    s = str(n)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

check(is_undulating)
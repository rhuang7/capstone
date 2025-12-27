def check(candidate):
    assert candidate("aaaa") == 1
    assert candidate("ab") == 2
    assert candidate("abc") == 3


def min_rotations_to_match(s):
    if not s:
        return 0
    n = len(s)
    for i in range(1, n):
        if s[i:] + s[:i] == s:
            return i
    return n

check(min_rotations_to_match)
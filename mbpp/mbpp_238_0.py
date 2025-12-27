def check(candidate):
    assert candidate("abc") == 6
    assert candidate("abcd") == 10
    assert candidate("abcde") == 15


def count_non_empty_substrings(s):
    return len(s) * (len(s) + 1) // 2

check(count_non_empty_substrings)
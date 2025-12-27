def check(candidate):
    assert candidate("abcabc") == None
    assert candidate("abc") == "a"
    assert candidate("ababc") == "c"


def first_non_repeated_char(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

check(first_non_repeated_char)
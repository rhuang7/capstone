def check(candidate):
    assert candidate("abcabc") == "a"
    assert candidate("abc") == "None"
    assert candidate("123123") == "1"


def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

check(first_repeated_char)
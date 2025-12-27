def check(candidate):
    assert candidate("Google") == "o"
    assert candidate("data") == "a"
    assert candidate("python") == '\0'


def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

check(first_repeated_char)
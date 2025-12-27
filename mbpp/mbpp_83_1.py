def check(candidate):
    assert candidate("abc") == "f"
    assert candidate("gfg") == "t"
    assert candidate("ab") == "c"


def sum_string_chars(s):
    if not s:
        return ''
    result = ''
    for char in s:
        result += char
    return result

check(sum_string_chars)
def check(candidate):
    assert candidate("01010101010") == "Yes"
    assert candidate("name0") == "No"
    assert candidate("101") == "Yes"


def is_binary_string(s):
    return all(c in '01' for c in s)

check(is_binary_string)
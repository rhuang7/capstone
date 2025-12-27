def check(candidate):
    assert candidate("a b c") == "abc"
    assert candidate("1 2 3") == "123"
    assert candidate(" b c") == "bc"


def remove_spaces(s):
    return s.replace(" ", "")

check(remove_spaces)
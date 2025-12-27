def check(candidate):
    assert candidate('A')==65
    assert candidate('R')==82
    assert candidate('S')==83


def get_ascii_value(char):
    return ord(char)

check(get_ascii_value)
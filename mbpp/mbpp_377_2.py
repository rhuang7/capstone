def check(candidate):
    assert candidate("aba",'a') == "b"
    assert candidate("toggle",'g') == "tole"
    assert candidate("aabbc",'b') == "aac"


def remove_char(s, char):
    return s.replace(char, '')

check(remove_char)
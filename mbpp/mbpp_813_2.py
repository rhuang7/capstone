def check(candidate):
    assert candidate('python')==6
    assert candidate('program')==7
    assert candidate('language')==8


def string_length(s):
    return len(s)

check(string_length)
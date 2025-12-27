def check(candidate):
    assert candidate("cba") == "abc"
    assert candidate("data") == "aadt"
    assert candidate("zxy") == "xyz"


def sort_string(s):
    return ''.join(sorted(s))

check(sort_string)
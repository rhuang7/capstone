def check(candidate):
    assert candidate("data") == "a"
    assert candidate("create") == "e"
    assert candidate("brilliant girl") == "i"


def max_occuring_char(s):
    from collections import Counter
    return Counter(s).most_common(1)[0][0] if s else None

check(max_occuring_char)
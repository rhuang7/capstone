def check(candidate):
    assert candidate("hello world")==('l')
    assert candidate("hello ")==('l')
    assert candidate("python pr")==('p')


def most_common_char(s):
    from collections import Counter
    return Counter(s).most_common(1)[0][0] if s else None

check(most_common_char)
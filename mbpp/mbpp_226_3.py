def check(candidate):
    assert candidate('abcdef') == 'ace'
    assert candidate('python') == 'pto'
    assert candidate('data') == 'dt'


def remove_odd_indexed_characters(s):
    return s[::2]

check(remove_odd_indexed_characters)
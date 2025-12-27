def check(candidate):
    assert candidate('peep','e') == 'pep'
    assert candidate('Greek','e') == 'Grek'
    assert candidate('Moon','o') == 'Mon'


def replace_multiple_occurrences(s, char):
    result = ""
    prev_char = None
    for c in s:
        if c == char and prev_char == char:
            continue
        result += c
        prev_char = c
    return result

check(replace_multiple_occurrences)
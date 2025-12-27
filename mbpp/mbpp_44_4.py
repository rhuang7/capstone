def check(candidate):
    assert candidate(" python")==('Not matched!')
    assert candidate("python")==('Found a match!')
    assert candidate("  lang")==('Not matched!')


def match_word_at_start(s):
    import re
    return bool(re.match(r'\b\w+\b', s))

check(match_word_at_start)
def check(candidate):
    assert candidate("python.")==('Found a match!')
    assert candidate("python.")==('Found a match!')
    assert candidate("  lang  .")==('Not matched!')


def match_word_at_end(s):
    import re
    pattern = r'\b\w+(?:[^\w\s])?$'
    return re.search(pattern, s) is not None

check(match_word_at_end)
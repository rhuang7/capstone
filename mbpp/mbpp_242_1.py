def check(candidate):
    assert candidate("python programming")==18
    assert candidate("language")==8
    assert candidate("words")==5


def count_total_characters(s):
    return len(s)

check(count_total_characters)
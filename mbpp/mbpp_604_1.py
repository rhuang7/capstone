def check(candidate):
    assert candidate("python program")==("program python")
    assert candidate("java language")==("language java")
    assert candidate("indian man")==("man indian")


def reverse_words(s):
    return ' '.join(reversed(s.split()))

check(reverse_words)
def check(candidate):
    assert candidate("python language") == 8
    assert candidate("PHP") == 3
    assert candidate("") == 0


def length_of_last_word(s):
    words = s.strip().split()
    if words:
        return len(words[-1])
    return 0

check(length_of_last_word)
def check(candidate):
    assert candidate("ab ca bc ab") == "ab"
    assert candidate("ab ca bc") == 'None'
    assert candidate("ab ca bc ca ab bc") == "ca"


def first_repeated_word(s):
    words = s.split()
    seen = set()
    for word in words:
        if word in seen:
            return word
        seen.add(word)
    return None

check(first_repeated_word)
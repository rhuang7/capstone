def check(candidate):
    assert candidate("Hadoop") == False
    assert candidate("great") == True
    assert candidate("structure") == True


def is_word_length_odd(word):
    return len(word) % 2 == 1

check(is_word_length_odd)
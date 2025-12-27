def check(candidate):
    assert candidate("program") == False
    assert candidate("solution") == True
    assert candidate("data") == True


def is_word_length_even(word):
    return len(word) % 2 == 0

check(is_word_length_even)
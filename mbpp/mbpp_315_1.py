def check(candidate):
    assert candidate("python language") == "language"
    assert candidate("maximum even length") == "length"
    assert candidate("eve") == "-1"


def find_first_max_even_word_length(words):
    max_length = 0
    result = ""
    for word in words:
        if word.isdigit():
            continue
        if word.isalpha():
            if len(word) > max_length and len(word) % 2 == 0:
                max_length = len(word)
                result = word
    return result

check(find_first_max_even_word_length)
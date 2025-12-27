def check(candidate):
    assert candidate(["win","lose","great"]) == 3
    assert candidate(["a","ab","abc"]) == 1
    assert candidate(["12","12","1234"]) == 2


def shortest_word_length(words):
    if not words:
        return 0
    return min(len(word) for word in words)

check(shortest_word_length)
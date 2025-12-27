def check(candidate):
    assert candidate(["python","PHP","bigdata"]) == 7
    assert candidate(["a","ab","abc"]) == 3
    assert candidate(["small","big","tall"]) == 5


def longest_word_length(words):
    if not words:
        return 0
    return max(len(word) for word in words)

check(longest_word_length)
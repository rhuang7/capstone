def check(candidate):
    assert candidate("python is a programming language",1)==[('python', 1)]
    assert candidate("python is a programming language",1)==[('python', 1)]
    assert candidate("python is a programming language",5)==[('python', 1),('is', 1), ('a', 1), ('programming', 1), ('language', 1)]


def most_common_words(text, n):
    from collections import Counter
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

check(most_common_words)
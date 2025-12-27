def check(candidate):
    assert candidate(3,"python is a programming language")==['python','programming','language']
    assert candidate(2,"writing a program")==['writing','program']
    assert candidate(5,"sorting list")==['sorting']


def shortlist_words(words, n):
    return [word for word in words if len(word) > n]

check(shortlist_words)
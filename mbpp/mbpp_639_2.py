def check(candidate):
    assert candidate(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert candidate(["php", "res", "Python", "abcd", "Java", "aaa"])==10
    assert candidate(["abcd", "Python", "abba", "aba"])==6


def sum_lengths_after_filtering(names):
    return sum(len(name) for name in names if name[0].isupper())

check(sum_lengths_after_filtering)
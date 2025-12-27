def check(candidate):
    assert candidate(["php", "res", "Python", "abcd", "Java", "aaa"])==['php', 'aaa']
    assert candidate(["abcd", "Python", "abba", "aba"])==['abba', 'aba']
    assert candidate(["abcd", "abbccbba", "abba", "aba"])==['abbccbba', 'abba', 'aba']


def find_palindromes(strings):
    return list(filter(lambda s: s == s[::-1], strings))

check(find_palindromes)
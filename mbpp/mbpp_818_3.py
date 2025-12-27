def check(candidate):
    assert candidate('abc') == 3
    assert candidate('string') == 6
    assert candidate('Python') == 5


def count_lowercase_letters(s):
    return sum(1 for char in s if char.islower())

check(count_lowercase_letters)
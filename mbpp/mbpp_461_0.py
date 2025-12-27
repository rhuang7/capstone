def check(candidate):
    assert candidate('PYthon') == 1
    assert candidate('BigData') == 1
    assert candidate('program') == 0


def count_uppercase(s):
    return sum(1 for char in s if char.isupper())

check(count_uppercase)
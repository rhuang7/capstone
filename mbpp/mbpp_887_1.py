def check(candidate):
    assert candidate(5) == True
    assert candidate(6) == False
    assert candidate(7) == True


def is_odd(number):
    return (number & 1) == 1

check(is_odd)
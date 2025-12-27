def check(candidate):
    assert candidate(1) == False
    assert candidate(2) == True
    assert candidate(3) == False


def is_even(number):
    return (number & 1) == 0

check(is_even)
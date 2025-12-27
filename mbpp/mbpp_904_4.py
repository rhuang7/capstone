def check(candidate):
    assert candidate(13.5)==False
    assert candidate(0)==True
    assert candidate(-9)==False


def is_even(number):
    return number % 2 == 0

check(is_even)
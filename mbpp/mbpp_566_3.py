def check(candidate):
    assert candidate(345)==12
    assert candidate(12)==3
    assert candidate(97)==16


def sum_digits(n):
    return sum(int(digit) for digit in str(n))

check(sum_digits)
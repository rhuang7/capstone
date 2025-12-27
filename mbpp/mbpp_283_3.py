def check(candidate):
    assert candidate(1234) == True
    assert candidate(51241) == False
    assert candidate(321) == True


def is_valid_number(n):
    from collections import Counter

    if n < 0:
        return False

    digit_count = Counter(str(n))
    for digit, count in digit_count.items():
        if int(digit) < count:
            return False
    return True

check(is_valid_number)
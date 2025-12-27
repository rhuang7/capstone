def check(candidate):
    assert candidate(12345) == 5
    assert candidate(11223305) == 8
    assert candidate(4123459) == 7


def count_digits(number):
    if number == 0:
        return 1
    count = 0
    number = abs(number)
    while number > 0:
        number //= 10
        count += 1
    return count

check(count_digits)
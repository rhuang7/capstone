def check(candidate):
    assert candidate(7) == 4
    assert candidate(5) == 3
    assert candidate(4) == 2


def count_digits_in_factorial(n):
    import math
    if n < 0:
        return 0
    # Using Kamenetsky's formula to estimate the number of digits
    if n == 0 or n == 1:
        return 1
    digits = int(n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2)
    return digits

check(count_digits_in_factorial)
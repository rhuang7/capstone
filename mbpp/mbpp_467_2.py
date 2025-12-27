def check(candidate):
    assert candidate(10) == 12
    assert candidate(2) == 2
    assert candidate(33) == 41


def decimal_to_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal

check(decimal_to_octal)
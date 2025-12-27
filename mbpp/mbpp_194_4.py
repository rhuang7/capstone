def check(candidate):
    assert candidate(25) == 21
    assert candidate(30) == 24
    assert candidate(40) == 32


def octal_to_decimal(octal_str):
    return int(octal_str, 8)

check(octal_to_decimal)
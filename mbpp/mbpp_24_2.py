def check(candidate):
    assert candidate(100) == 4
    assert candidate(1011) == 11
    assert candidate(1101101) == 109


def binary_to_decimal(binary_str):
    return int(binary_str, 2)

check(binary_to_decimal)
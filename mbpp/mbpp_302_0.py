def check(candidate):
    assert candidate(6) == 4
    assert candidate(10) == 8
    assert candidate(18) == 16


def most_significant_set_bit(n):
    if n == 0:
        return 0
    bit_position = 0
    while n > 0:
        n >>= 1
        bit_position += 1
    return bit_position

check(most_significant_set_bit)
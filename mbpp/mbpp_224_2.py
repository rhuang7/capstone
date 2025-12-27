def check(candidate):
    assert candidate(2) == 1
    assert candidate(4) == 1
    assert candidate(6) == 2


def count_set_bits(n):
    return bin(n).count('1')

check(count_set_bits)
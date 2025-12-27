def check(candidate):
    assert candidate(10) == 15
    assert candidate(20) == 21
    assert candidate(30) == 31


def set_odd_bits(n):
    return n | 0xAAAAAAAA

check(set_odd_bits)
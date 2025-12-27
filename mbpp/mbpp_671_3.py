def check(candidate):
    assert candidate(21) == 23
    assert candidate(11) == 15
    assert candidate(15) == 15


def set_rightmost_unset_bit(n):
    return n | (n + 1)

check(set_rightmost_unset_bit)
def check(candidate):
    assert candidate(12) == 3
    assert candidate(18) == 2
    assert candidate(16) == 5


def rightmost_set_bit_position(n):
    if n == 0:
        return -1  # No set bits
    return (n & -n).bit_length() - 1

check(rightmost_set_bit_position)
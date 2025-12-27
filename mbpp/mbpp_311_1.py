def check(candidate):
    assert candidate(10) == 14
    assert candidate(12) == 14
    assert candidate(15) == 15


def set_leftmost_unset_bit(n):
    # Find the position of the leftmost unset bit
    # This is done by finding the first 0 in the binary representation from left to right
    # We can use bit manipulation to find the leftmost 0
    # The leftmost unset bit is the position of the first 0 when we count from the left
    # We can use the formula: (n ^ (n & (n + 1))) to find the rightmost 0
    # But to find the leftmost 0, we need to find the position of the highest set bit in (n ^ (n + 1))
    # Then we can set that bit
    # Alternatively, we can use the bit_length of n to find the position of the leftmost 0
    # For example, if n is 0, the leftmost unset bit is at position 0
    # For n > 0, the leftmost unset bit is at position (bit_length of n) - 1
    # So we can set that bit
    if n == 0:
        return 1
    # Find the position of the leftmost unset bit
    leftmost_unset_bit_pos = (n.bit_length() - 1)
    # Set that bit
    return n | (1 << leftmost_unset_bit_pos)

check(set_leftmost_unset_bit)
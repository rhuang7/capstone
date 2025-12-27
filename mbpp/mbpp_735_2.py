def check(candidate):
    assert candidate(9) == 15
    assert candidate(10) == 12
    assert candidate(11) == 13


def toggle_middle_bits(n):
    if n < 2:
        return n  # No middle bits to toggle if n has only 1 or 0 bits
    
    # Mask to toggle all bits except the first and last
    # For example, if n is 8 (1000 in binary), mask is 0111 (7)
    # For n with k bits, mask is (1 << (k - 2)) - 1
    k = n.bit_length()
    mask = (1 << (k - 2)) - 1
    
    return n ^ mask

check(toggle_middle_bits)
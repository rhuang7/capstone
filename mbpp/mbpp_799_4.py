def check(candidate):
    assert candidate(16,2) == 64
    assert candidate(10,2) == 40
    assert candidate(99,3) == 792


def left_rotate_bits(n, rotations):
    # Get the number of bits in the number
    num_bits = n.bit_length()
    
    # Perform the left rotation
    rotated = (n << rotations) & ((1 << num_bits) - 1)
    rotated |= (n >> (num_bits - rotations)) if rotations != num_bits else 0
    
    return rotated

check(left_rotate_bits)
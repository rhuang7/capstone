def check(candidate):
    assert candidate(10) == 3
    assert candidate(15) == 6
    assert candidate(20) == 5


def toggle_first_last_bit(n):
    # Check if the number is at least 1 (to have at least two bits)
    if n < 1:
        return n
    
    # Toggle the first bit (LSB)
    n ^= 1
    
    # Toggle the last bit (MSB)
    # Find the position of the highest set bit
    highest_bit = n.bit_length()
    n ^= (1 << (highest_bit - 1))
    
    return n

check(toggle_first_last_bit)
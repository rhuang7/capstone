def check(candidate):
    assert candidate(10) == 15
    assert candidate(20) == 1
    assert candidate(30) == 11


def toggle_odd_bits(n):
    # Create a mask with all odd bits set to 1
    mask = 0xAAAAAAAA
    # Toggle the odd bits using XOR
    return n ^ mask

check(toggle_odd_bits)
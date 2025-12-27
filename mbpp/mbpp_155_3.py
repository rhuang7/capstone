def check(candidate):
    assert candidate(10) == 0
    assert candidate(20) == 30
    assert candidate(30) == 20


def toggle_even_bits(n):
    # Create a mask with all even bits set to 1
    mask = 0xAAAAAAAA
    # Toggle even bits using XOR
    return n ^ mask

check(toggle_even_bits)
def check(candidate):
    assert candidate(10) == 10
    assert candidate(20) == 30
    assert candidate(30) == 30


def set_even_bits(number):
    # Create a mask with all even bits set to 1
    mask = 0xAAAAAAAA  # This is 10101010... in binary, which is even bits
    # Apply the mask to set even bits of the number
    return number | mask

check(set_even_bits)
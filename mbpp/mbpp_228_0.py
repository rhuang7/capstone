def check(candidate):
    assert candidate(4,1,2) == True
    assert candidate(17,2,4) == True
    assert candidate(39,4,6) == False


def are_all_bits_unset(n, start, end):
    # Create a mask to check the bits in the specified range
    mask = ( (1 << end) - 1 ) ^ ( (1 << start) - 1 )
    # Check if the AND of n and mask is 0
    return (n & mask) == 0

check(are_all_bits_unset)
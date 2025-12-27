def check(candidate):
    assert candidate(10,2,1) == True 
    assert candidate(5,2,4) == False
    assert candidate(22,2,3) == True 


def are_all_bits_within_range(number, start, end):
    """
    Check if all the bits of a number are within a specified range [start, end].
    """
    # Check if the number is non-negative
    if number < 0:
        return False
    
    # Extract the bits of the number
    bits = []
    while number > 0:
        bits.append(number % 2)
        number = number // 2
    
    # Check if all bits are within the given range
    for bit in bits:
        if not (start <= bit <= end):
            return False
    
    return True

check(are_all_bits_within_range)
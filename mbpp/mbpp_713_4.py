def check(candidate):
    assert candidate((True, True, True, True) ) == True
    assert candidate((True, False, True, True) ) == False
    assert candidate((True, True, True, True) ) == True


def is_valid_tuple(t):
    # Check if the tuple contains exactly three elements
    if len(t) != 3:
        return False
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in t):
        return False
    
    # Check if all elements are non-negative
    if any(x < 0 for x in t):
        return False
    
    return True

check(is_valid_tuple)
def check(candidate):
    assert candidate([2,3,4], [2,3,8]) == True
    assert candidate([2,3,4], [4,-3,8]) == False
    assert candidate([3,3],[5,5]) == True


def are_parallel(line1, line2):
    """
    Check if two lines are parallel.
    
    Each line is represented as a tuple (a, b, c), where the line equation is ax + by + c = 0.
    Two lines are parallel if their normal vectors (a, b) are scalar multiples of each other.
    """
    a1, b1, _ = line1
    a2, b2, _ = line2
    
    # Check if the direction vectors are scalar multiples
    # To avoid division by zero, check if (a1 * b2) == (a2 * b1)
    return a1 * b2 == a2 * b1

check(are_parallel)
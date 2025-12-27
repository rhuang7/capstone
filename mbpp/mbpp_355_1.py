def check(candidate):
    assert candidate(2) == 8
    assert candidate(1) == 1
    assert candidate(0) == 0


def count_rectangles_in_circle(r):
    import math
    
    # The maximum possible side length of a rectangle that can fit in a circle
    # is the diameter of the circle (2r)
    max_side = 2 * r
    
    count = 0
    
    # Iterate over possible side lengths of rectangles
    for side in range(1, int(max_side) + 1):
        # For each side length, calculate the maximum possible other side
        # such that the rectangle fits in the circle
        max_other_side = math.sqrt((2 * r)**2 - side**2)
        
        # Count the number of integer side lengths that can form a rectangle
        # with the current side length
        count += int(max_other_side)
    
    return count

check(count_rectangles_in_circle)
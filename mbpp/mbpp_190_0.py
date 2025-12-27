def check(candidate):
    assert candidate(1,1,4,4) == 4
    assert candidate(1,2,1,2) == 1
    assert candidate(4,2,6,4) == 1


def count_integral_coordinates_in_square(x1, y1, x2, y2):
    # Check if the square is valid (x1 < x2 and y1 < y2)
    if x1 >= x2 or y1 >= y2:
        return 0
    
    # Calculate the number of integral coordinates inside the square
    # The number of points is (x2 - x1) * (y2 - y1)
    return (x2 - x1) * (y2 - y1)

check(count_integral_coordinates_in_square)
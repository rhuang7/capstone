def check(candidate):
    assert candidate(4,2,2,5) == -1.5
    assert candidate(2,4,4,6) == 1
    assert candidate(1,2,4,2) == 0


def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return None  # Undefined slope (vertical line)
    return (y2 - y1) / (x2 - x1)

check(calculate_slope)
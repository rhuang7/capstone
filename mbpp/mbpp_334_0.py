def check(candidate):
    assert candidate(1,2,3) == False
    assert candidate(2,3,5) == False
    assert candidate(7,10,5) == True


def is_valid_triangle(a, b, c):
    # Check if all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Check triangle inequality theorem
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

check(is_valid_triangle)
def check(candidate):
    assert candidate(6,8,12)==False 
    assert candidate(6,6,12)==False
    assert candidate(6,6,6)==True


def is_equilateral(side1, side2, side3):
    return side1 == side2 == side3

check(is_equilateral)
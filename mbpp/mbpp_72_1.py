def check(candidate):
    assert candidate(5) == True
    assert candidate(10) == False
    assert candidate(15) == True


def can_be_difference_of_squares(n):
    if n < 0:
        return False
    for i in range(1, n + 1):
        if i * i - (i - 1) * (i - 1) == n:
            return True
    return False

check(can_be_difference_of_squares)
def check(candidate):
    assert candidate(1,1,1) == 3
    assert candidate(-1,-2,-3) == 0
    assert candidate(1,2,2) == 2


def count_equal_numbers(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

check(count_equal_numbers)
def check(candidate):
    assert candidate(5,10) == 10
    assert candidate(-1,-2) == -1
    assert candidate(9,7) == 9


def max_of_two(a, b):
    return a if a > b else b

check(max_of_two)
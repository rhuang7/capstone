def check(candidate):
    assert candidate(10,20)==20
    assert candidate(19,15)==19
    assert candidate(-10,-20)==-10


def max_of_two(a, b):
    return a if a > b else b

check(max_of_two)
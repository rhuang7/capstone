def check(candidate):
    assert candidate(3,3) == 0
    assert candidate(10,3) == 1
    assert candidate(16,5) == 1


def find_remainder(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a % b

check(find_remainder)
def check(candidate):
    assert candidate(10,3) == 3
    assert candidate(4,2) == 2
    assert candidate(20,5) == 4


def find_quotient(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a // b

check(find_quotient)
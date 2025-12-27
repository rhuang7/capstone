def check(candidate):
    assert candidate(4) == 12
    assert candidate(7) == 169
    assert candidate(8) == 408


def pell_number(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a * 2 + b
    return b

check(pell_number)
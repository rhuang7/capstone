def check(candidate):
    assert candidate(7) == 13
    assert candidate(8) == 21
    assert candidate(9) == 34


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

check(fibonacci)
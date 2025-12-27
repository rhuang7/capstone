def check(candidate):
    assert candidate(10) == 5
    assert candidate(15) == 5
    assert candidate(5) == 4


def first_factorial_divisible_by_x(x):
    if x < 1:
        return None  # x must be a natural number
    
    n = 1
    while True:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        if factorial % x == 0:
            return n
        n += 1

check(first_factorial_divisible_by_x)
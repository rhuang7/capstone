def check(candidate):
    assert candidate(5) == 1
    assert candidate(10) == 3
    assert candidate(7) == 5


def first_digit_of_factorial(n):
    if n < 0:
        return None  # Factorial is undefined for negative numbers
    if n == 0 or n == 1:
        return 1
    # Use logarithms to avoid overflow
    log_sum = 0.0
    for i in range(2, n + 1):
        log_sum += math.log10(i)
    first_digit = 10 ** (log_sum % 1)
    return int(first_digit)

check(first_digit_of_factorial)
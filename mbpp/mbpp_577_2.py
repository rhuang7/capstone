def check(candidate):
    assert candidate(4) == 4
    assert candidate(21) == 0
    assert candidate(30) == 0


def last_digit_of_factorial(n):
    if n < 0:
        return -1  # Factorial is undefined for negative numbers
    if n == 0 or n == 1:
        return 0
    # For n >= 5, the last digit of factorial is always 0
    if n >= 5:
        return 0
    # Compute factorial and return last digit for n < 5
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % 10
    return result

check(last_digit_of_factorial)
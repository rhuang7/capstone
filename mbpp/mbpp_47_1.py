def check(candidate):
    assert candidate(2,4) == 2
    assert candidate(6,8) == 6
    assert candidate(1,2) == 2


def last_digit_of_factorial_division(a, b):
    if a > b:
        return 0  # factorial of a cannot divide factorial of b if a > b
    # Compute the last digit of (b! / a!)
    # This is equivalent to the last digit of (b * (b-1) * ... * (a+1))
    product = 1
    for i in range(a + 1, b + 1):
        product = (product * i) % 10
    return product

check(last_digit_of_factorial_division)
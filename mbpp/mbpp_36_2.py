def check(candidate):
    assert candidate(1,2,1) == 5
    assert candidate(3,5,1) == 6
    assert candidate(5,6,5) == 3


def get_nth_digit(numerator, denominator, n):
    # Calculate the fractional part
    fractional_part = numerator / denominator - int(numerator / denominator)
    
    # Find the nth digit in the fractional part
    digit = 0
    for _ in range(n):
        fractional_part *= 10
        digit = int(fractional_part)
        fractional_part = fractional_part - digit
    
    return digit

check(get_nth_digit)
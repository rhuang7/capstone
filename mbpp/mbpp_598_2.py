def check(candidate):
    assert candidate(153)==True
    assert candidate(259)==False
    assert candidate(4458)==False


def is_armstrong_number(n):
    # Convert the number to a string to iterate over its digits
    digits = str(n)
    # Get the number of digits
    length = len(digits)
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** length for digit in digits)
    # Check if the sum equals the original number
    return sum_of_powers == n

check(is_armstrong_number)
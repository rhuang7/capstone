def check(candidate):
    assert candidate(2841) == True
    assert candidate(1234) == False
    assert candidate(1212) == False


def product_of_digits_at_even_odd_positions(n):
    # Convert the number to a string to iterate over each digit
    digits = str(n)
    product_even = 1
    product_odd = 1
    
    # Iterate over each digit, checking if the position is even or odd
    for i in range(len(digits)):
        digit = int(digits[i])
        if (i + 1) % 2 == 0:  # Even position (1-based index)
            product_even *= digit
        else:  # Odd position (1-based index)
            product_odd *= digit
    
    return product_even == product_odd

check(product_of_digits_at_even_odd_positions)
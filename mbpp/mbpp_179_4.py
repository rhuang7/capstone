def check(candidate):
    assert candidate(14) == True
    assert candidate(12) == False
    assert candidate(197) == True


def is_keith_number(n):
    # Handle edge cases
    if n < 1:
        return False
    
    # Convert number to string to split into digits
    digits = list(map(int, str(n)))
    length = len(digits)
    
    # Initialize sum with the digits
    keith_sum = sum(digits)
    
    # Iterate to check if the number appears again
    for _ in range(length):
        # Check if current sum equals the original number
        if keith_sum == n:
            return True
        # Update sum with the last digit
        keith_sum = keith_sum + digits[-1]
        # Remove the first digit
        digits.pop(0)
    
    return False

check(is_keith_number)
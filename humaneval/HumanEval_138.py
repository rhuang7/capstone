def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True



def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # For a number to be expressed as the sum of 4 positive even numbers, it must be at least 8 (2+2+2+2)
    # Also, since even + even = even, the sum of 4 even numbers will always be even
    # So, n must be even and at least 8
    return n >= 8 and n % 2 == 0

check(is_equal_to_sum_even)
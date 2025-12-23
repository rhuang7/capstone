def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"



def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only the number 1 satisfies the condition
    # For n-digit numbers, the first digit can be 1 (1 choice)
    # The last digit can be 1 (1 choice)
    # However, we must subtract the overlap where both first and last digits are 1
    # Total = start_with_1 + end_with_1 - both_start_and_end_with_1
    start_with_1 = 1 * 10 ** (n - 1)
    end_with_1 = 9 * 1 * 10 ** (n - 2)
    both_start_and_end_with_1 = 1 * 1 * 10 ** (n - 2)
    return start_with_1 + end_with_1 - both_start_and_end_with_1

check(starts_one_ends)
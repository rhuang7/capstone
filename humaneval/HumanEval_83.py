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
        return 1  # Only number is 1, which starts and ends with 1
    count = 0
    # Numbers that start with 1
    count += 10 ** (n - 1)
    # Numbers that end with 1
    count += 10 ** (n - 1)
    # Subtract the overlap (numbers that both start and end with 1)
    count -= 10 ** (n - 2)
    return count

check(starts_one_ends)
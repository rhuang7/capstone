def check(candidate):
    assert candidate(10) == True
    assert candidate(7) == False
    assert candidate(14) == True


def is_sum_of_non_zero_powers_of_two(n):
    if n <= 0:
        return False
    # Check if the number has any bit set in its binary representation
    # If it does, then it can be represented as sum of non-zero powers of 2
    return n != 0 and (n & (n - 1)) != 0

check(is_sum_of_non_zero_powers_of_two)
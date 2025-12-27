def check(candidate):
    assert candidate(70) == False
    assert candidate(23) == False
    assert candidate(73) == True


def is_one_less_than_twice_reverse(n):
    # Handle negative numbers by taking absolute value
    n = abs(n)
    # Convert number to string to reverse it
    reversed_str = str(n)[::-1]
    # Convert reversed string back to integer
    reversed_num = int(reversed_str)
    # Check if the original number is one less than twice the reversed number
    return n == 2 * reversed_num - 1

check(is_one_less_than_twice_reverse)
def check(candidate):
    assert candidate([1,2,3],3) == 321
    assert candidate([4,5,6,1],4) == 6541
    assert candidate([1,2,3,9],4) == 9321


def largest_number(digits):
    # Sort the digits in descending order
    digits.sort(reverse=True)
    # Join the sorted digits into a string
    largest = ''.join(digits)
    return largest

check(largest_number)
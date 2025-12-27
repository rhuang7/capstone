def check(candidate):
    assert candidate([1,2,3,-4,-6]) == -6
    assert candidate([1,2,3,-8,-9]) == -9
    assert candidate([1,2,3,4,-1]) == -1


def find_largest_negative(numbers):
    negative_numbers = [num for num in numbers if num < 0]
    if not negative_numbers:
        return None
    return max(negative_numbers)

check(find_largest_negative)
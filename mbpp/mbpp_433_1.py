def check(candidate):
    assert candidate([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'
    assert candidate([2, 3, 4, 5, 6], 8) == 'Yes, the entered number is greater than those in the array'
    assert candidate([9, 7, 4, 8, 6, 1], 11) == 'Yes, the entered number is greater than those in the array'


def is_number_greater_than_all(numbers, num):
    for n in numbers:
        if num <= n:
            return False
    return True

check(is_number_greater_than_all)
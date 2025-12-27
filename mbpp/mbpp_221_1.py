def check(candidate):
    assert candidate ([1, 3, 5, 7, 4, 1, 6, 8]) == 4
    assert candidate([2, 3, 4]) == 2
    assert candidate([5, 6, 7]) == 6


def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

check(find_first_even)
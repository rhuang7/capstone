def check(candidate):
    assert candidate([1,-2,3,-4]) == 2
    assert candidate([3,4,5,-1]) == 3
    assert candidate([1,2,3,4]) == 4


def count_positive_numbers(numbers):
    return sum(1 for num in numbers if num > 0)

check(count_positive_numbers)
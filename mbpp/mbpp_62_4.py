def check(candidate):
    assert candidate([10, 20, 1, 45, 99]) == 1
    assert candidate([1, 2, 3]) == 1
    assert candidate([45, 46, 50, 60]) == 45


def find_smallest_number(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

check(find_smallest_number)
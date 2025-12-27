def check(candidate):
    assert candidate([1, 1, 3, 4, 4, 5, 6, 7])==[1, 3, 12, 16, 20, 30, 42]
    assert candidate([4, 5, 8, 9, 6, 10])==[20, 40, 72, 54, 60]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[2, 6, 12, 20, 30, 42, 56, 72, 90]


def multiply_consecutive_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

check(multiply_consecutive_numbers)
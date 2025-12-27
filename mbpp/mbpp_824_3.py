def check(candidate):
    assert candidate([1,3,5,2]) == [1,3,5]
    assert candidate([5,6,7]) == [5,7]
    assert candidate([1,2,3,4]) == [1,3]


def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

check(remove_even_numbers)
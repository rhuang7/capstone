def check(candidate):
    assert candidate([1,2,3]) == [2]
    assert candidate([2,4,6]) == [2,4,6]
    assert candidate([10,20,3]) == [10,20]


def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

check(remove_odd_numbers)
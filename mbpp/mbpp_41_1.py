def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[2, 4, 6, 8, 10]
    assert candidate([10,20,45,67,84,93])==[10,20,84]
    assert candidate([5,7,9,8,6,4,3])==[8,6,4]


def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

check(filter_even_numbers)
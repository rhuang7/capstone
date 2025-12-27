def check(candidate):
    assert candidate([1, 2, -8, -2, 0, -2])==-2
    assert candidate([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert candidate([2,2])==None


def second_smallest(numbers):
    if len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[1]

check(second_smallest)
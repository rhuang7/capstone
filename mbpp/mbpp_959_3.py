def check(candidate):
    assert candidate([15, 9, 55, 41, 35, 20, 62, 49]) == 35.75
    assert candidate([4, 5, 1, 2, 9, 7, 10, 8]) == 5.75
    assert candidate([1,2,3]) == 2


def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

check(find_average)
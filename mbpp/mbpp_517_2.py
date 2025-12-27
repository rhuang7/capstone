def check(candidate):
    assert candidate([1,2,3,4,-1]) == 4
    assert candidate([0,1,2,-5,-1,6]) == 6
    assert candidate([0,0,1,0]) == 1


def find_largest_positive(numbers):
    return max((num for num in numbers if num > 0), default=None)

check(find_largest_positive)
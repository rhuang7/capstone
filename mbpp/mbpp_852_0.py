def check(candidate):
    assert candidate([1,-2,3,-4]) == [1,3]
    assert candidate([1,2,3,-4]) == [1,2,3]
    assert candidate([4,5,-6,7,-8]) == [4,5,7]


def remove_negatives(lst):
    return [num for num in lst if num >= 0]

check(remove_negatives)
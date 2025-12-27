def check(candidate):
    assert candidate([1, 2, 3]) == 6
    assert candidate([15, 12, 13, 10]) == 50
    assert candidate([0, 1, 2]) == 3


def array_sum(arr):
    return sum(arr)

check(array_sum)
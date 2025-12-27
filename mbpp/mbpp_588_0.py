def check(candidate):
    assert candidate([1,2,3,4]) == 3
    assert candidate([4,5,12]) == 8
    assert candidate([9,2,3]) == 7


def find_difference(arr):
    return max(arr) - min(arr)

check(find_difference)
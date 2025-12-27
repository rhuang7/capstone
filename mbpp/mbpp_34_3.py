def check(candidate):
    assert candidate([1,2,3,5],4) == 4
    assert candidate([1,3,4,5],4) == 2
    assert candidate([1,2,3,5,6,7],5) == 4


def find_missing_number(sorted_array):
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
    return left

check(find_missing_number)
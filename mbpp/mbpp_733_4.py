def check(candidate):
    assert candidate([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert candidate([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert candidate([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4


def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

check(find_first_occurrence)
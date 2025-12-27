def check(candidate):
    assert candidate([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
    assert candidate([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
    assert candidate([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6


def find_last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

check(find_last_occurrence)
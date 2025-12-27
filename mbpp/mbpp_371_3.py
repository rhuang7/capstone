def check(candidate):
    assert candidate([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
    assert candidate([0, 1, 2, 6, 9, 11, 15], 0, 6) == 3
    assert candidate([1, 2, 3, 4, 6, 9, 11, 15], 0, 7) == 0


def smallest_missing(arr):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= mid:
            left = mid + 1
        else:
            right = mid
    return left

check(smallest_missing)
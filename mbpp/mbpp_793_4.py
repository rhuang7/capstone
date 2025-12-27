def check(candidate):
    assert candidate([1,2,3],1,3) == 0
    assert candidate([1,1,1,2,3,4],1,6) == 2
    assert candidate([2,3,2,3,6,8,9],3,8) == 3


def find_last_position(arr, target):
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

check(find_last_position)
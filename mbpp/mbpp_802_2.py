def check(candidate):
    assert candidate([3,2,1],3) == 1
    assert candidate([4,5,1,2,3],5) == 2
    assert candidate([7,8,9,1,2,3],6) == 3


def count_rotations(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left

check(count_rotations)
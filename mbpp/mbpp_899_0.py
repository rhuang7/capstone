def check(candidate):
    assert candidate([3,2,1,2,3,4],6) == True
    assert candidate([2,1,4,5,1],5) == True
    assert candidate([1,2,2,1,2,3],6) == True


def can_sort_by_corners(arr):
    if not arr:
        return True
    n = len(arr)
    sorted_arr = sorted(arr)
    left = 0
    right = n - 1
    i = 0
    j = n - 1
    while i < j:
        if arr[left] != sorted_arr[i]:
            return False
        if arr[right] != sorted_arr[j]:
            return False
        left += 1
        right -= 1
        i += 1
        j -= 1
    return True

check(can_sort_by_corners)
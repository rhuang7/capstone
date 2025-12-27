def check(candidate):
    assert candidate([2,3,5,6,9],0,4) == 9
    assert candidate([3,4,5,2,1],0,4) == 5
    assert candidate([1,2,3],0,2) == 3


def find_max_in_rotated_sorted_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]

check(find_max_in_rotated_sorted_array)
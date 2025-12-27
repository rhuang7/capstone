def check(candidate):
    assert candidate([1,2,3,5,8], 6) == False
    assert candidate([7, 8, 9, 10, 13], 10) == True
    assert candidate([11, 13, 14, 19, 22, 36], 23) == False


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

check(binary_search)
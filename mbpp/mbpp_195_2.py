def check(candidate):
    assert candidate([1,2,3,4,5,6,6],6,6) == 5
    assert candidate([1,2,2,2,3,2,2,4,2],2,9) == 1
    assert candidate([1,2,3],1,3) == 0


def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching to the left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

check(find_first_occurrence)
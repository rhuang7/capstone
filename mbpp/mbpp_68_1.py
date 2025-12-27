def check(candidate):
    assert candidate([6, 5, 4, 4]) == True
    assert candidate([1, 2, 2, 3]) == True
    assert candidate([1, 3, 2]) == False


def is_monotonic(arr):
    if not arr:
        return True
    increasing = True
    decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
        if arr[i] < arr[i-1]:
            increasing = False
    return increasing or decreasing

check(is_monotonic)
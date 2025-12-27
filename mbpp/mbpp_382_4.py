def check(candidate):
    assert candidate([8, 9, 10, 1, 2, 3, 4, 5, 6, 7]) == 3
    assert candidate([8, 9, 10,2, 5, 6]) == 3
    assert candidate([2, 5, 6, 8, 9, 10]) == 0


def count_rotations(arr):
    n = len(arr)
    if n == 0:
        return 0
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2
        next_idx = (mid + 1) % n
        
        if arr[mid] > arr[next_idx]:
            high = mid - 1
        else:
            low = mid + 1
    
    return low

check(count_rotations)
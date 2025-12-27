def check(candidate):
    assert candidate([1, 3, 20, 4, 1, 0], 6) == 2
    assert candidate([2, 3, 4, 5, 6], 5) == 4
    assert candidate([8, 9, 11, 12, 14, 15], 6) == 5 


def find_peak(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

check(find_peak)
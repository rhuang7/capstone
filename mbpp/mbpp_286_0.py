def check(candidate):
    assert candidate([10, 20, -30, -1], 4, 3) == 30
    assert candidate([-1, 10, 20], 3, 2) == 59
    assert candidate([-1, -2, -3], 3, 3) == -1


def largest_subarray_sum(arr, k):
    if k == 1:
        return max_subarray_sum(arr)
    
    total_sum = sum(arr)
    max_subarray = max_subarray_sum(arr)
    max_wraparound = 0
    
    for i in range(len(arr)):
        max_wraparound = max(max_wraparound, arr[i] + max_subarray_sum(arr[i+1:]))
    
    return max(max_subarray, total_sum - min_subarray_sum(arr) * (k - 1), max_wraparound)

def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

def min_subarray_sum(arr):
    min_current = min_global = arr[0]
    for num in arr[1:]:
        min_current = min(num, min_current + num)
        min_global = min(min_global, min_current)
    return min_global

check(min_subarray_sum)
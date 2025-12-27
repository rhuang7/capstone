def check(candidate):
    assert candidate([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert candidate([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert candidate([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10


def largest_sum_subarray(arr):
    if not arr:
        return 0
    
    max_current = max_global = arr[0]
    
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    
    return max_global

check(largest_sum_subarray)
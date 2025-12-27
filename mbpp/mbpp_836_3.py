def check(candidate):
    assert candidate([-2, -3, 4, -1, -2, 1, 5, -3],8) == 5
    assert candidate([1, -2, 1, 1, -2, 1],6) == 2
    assert candidate([-1, -2, 3, 4, 5],5) == 3


def max_subarray_length(arr):
    if not arr:
        return 0
    
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    max_start = 0
    max_end = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = end
        
        if current_sum < 0:
            current_sum = 0
            start = end + 1
    
    return max_end - max_start + 1

check(max_subarray_length)
def check(candidate):
    assert candidate([[1],[1,2]]) == 1
    assert candidate([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert candidate([[3,3,3],[4,4,4,4]]) == 3


def min_sublist_length(nums):
    if not nums:
        return 0
    
    min_len = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(len(nums)):
        current_sum += nums[end]
        
        while current_sum >= 0 and end - start + 1 < min_len:
            min_len = end - start + 1
            if current_sum == 0:
                break
            current_sum -= nums[start]
            start += 1
    
    return min_len if min_len != float('inf') else 0

check(min_sublist_length)
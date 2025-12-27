def check(candidate):
    assert candidate([1, 3, 6, 1, 0, 9], 6) == 3
    assert candidate([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11) == 3
    assert candidate([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 10


def min_jumps(nums):
    if not nums or nums[0] == 0:
        return -1
    
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= n - 1:
                break
                
    return jumps if current_end >= n - 1 else -1

check(min_jumps)
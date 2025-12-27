def check(candidate):
    assert candidate([ 1, 3, 6, 13, 17, 18 ], 6) == 4
    assert candidate([10, 5, 3, 15, 20], 5) == 3
    assert candidate([18, 1, 3, 6, 13, 17], 6) == 4


def largest_divisible_subset(nums):
    if not nums:
        return []
    
    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
    
    max_len = max(dp)
    index = dp.index(max_len)
    
    result = []
    while index != -1:
        result.append(nums[index])
        index = prev[index]
    
    return result[::-1]

check(largest_divisible_subset)
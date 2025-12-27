def check(candidate):
    assert candidate([100, 1000, 100, 1000, 1], 5) == 2101
    assert candidate([3000, 2000, 1000, 3, 10], 5) == 5013
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8], 8) == 27


def max_sum_no_three_consecutive(nums):
    if not nums:
        return 0
    
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums)
    
    # dp[i] represents the maximum sum up to index i
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        # We can take nums[i] and add it to the max sum up to i-2
        # or skip nums[i] and take the max sum up to i-1
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

check(max_sum_no_three_consecutive)
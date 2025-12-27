def check(candidate):
    assert candidate([1, 2, 9, 4, 5, 0, 4, 11, 6]) == 26
    assert candidate([1, 2, 9, 5, 6, 0, 5, 12, 7]) == 28
    assert candidate([1, 3, 10, 5, 6, 0, 6, 14, 21]) == 44


def max_subsequence_sum(arr):
    if not arr:
        return 0
    
    n = len(arr)
    # dp[i] represents the maximum sum for the first i elements
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 0
    dp[1] = arr[0]
    
    for i in range(2, n + 1):
        # Either take the current element and add to the sum before the previous one
        # or skip the current element and take the sum up to i-1
        dp[i] = max(arr[i-1] + dp[i-2], dp[i-1])
    
    return dp[n]

check(max_subsequence_sum)
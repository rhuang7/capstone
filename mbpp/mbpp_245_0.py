def check(candidate):
    assert candidate([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
    assert candidate([80, 60, 30, 40, 20, 10], 6) == 210
    assert candidate([2, 3 ,14, 16, 21, 23, 29, 30], 8) == 138


def max_biotic_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # dp[i] represents the maximum sum of a bi-tonic subsequence ending at i
    dp = [0] * n
    
    # Calculate maximum sum of increasing subsequence ending at each index
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    # Calculate maximum sum of decreasing subsequence starting at each index
    dp2 = [0] * n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                dp2[i] = max(dp2[i], dp2[j] + arr[i])
    
    # The maximum bi-tonic sum is the maximum value in dp + dp2
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, dp[i] + dp2[i])
    
    return max_sum

check(max_biotic_sum)
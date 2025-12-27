def check(candidate):
    assert candidate([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert candidate([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert candidate([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71


def max_increasing_subsequence_with_kth_element(arr, k):
    n = len(arr)
    if k >= n or k <= 0:
        return 0  # Invalid k value
    
    # Calculate max increasing subsequence sum up to each index
    dp = [0] * n
    for i in range(n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    # Find the maximum sum including the kth element
    max_sum = 0
    for i in range(k):
        if arr[i] < arr[k]:
            max_sum = max(max_sum, dp[i] + arr[k])
    
    return max_sum

check(max_increasing_subsequence_with_kth_element)
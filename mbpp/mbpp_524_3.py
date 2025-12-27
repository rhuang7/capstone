def check(candidate):
    assert candidate([1, 101, 2, 3, 100, 4, 5], 7) == 106
    assert candidate([3, 4, 5, 10], 4) == 22
    assert candidate([10, 5, 4, 3], 4) == 10


def sum_of_max_increasing_subsequence(arr):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    
    for i in range(1, n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]
    
    return max(dp) if dp else 0

check(sum_of_max_increasing_subsequence)
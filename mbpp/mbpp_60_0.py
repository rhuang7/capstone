def check(candidate):
    assert candidate([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5
    assert candidate([-2, -1, 5, -1, 4, 0, 3], 7) == 4
    assert candidate([9, 11, 13, 15, 18], 5) == 1


def max_subsequence_length(arr):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n  # dp[i] represents the length of the longest subsequence ending at index i
    
    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) >= 1:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

check(max_subsequence_length)
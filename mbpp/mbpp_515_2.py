def check(candidate):
    assert candidate([3, 1, 7, 5], 4, 6) == True
    assert candidate([1, 7], 2, 5) == False
    assert candidate([1, 6], 2, 5) == False


def subset_sum_divisible_by_m(arr, m):
    n = len(arr)
    dp = [False] * (m)
    dp[0] = True
    
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if dp[j] and j + arr[i] < m:
                dp[j + arr[i]] = True
                
    return any(dp)

check(subset_sum_divisible_by_m)
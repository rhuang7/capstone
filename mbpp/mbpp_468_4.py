def check(candidate):
    assert candidate([3, 100, 4, 5, 150, 6], 6) == 45000 
    assert candidate([4, 42, 55, 68, 80], 5) == 50265600
    assert candidate([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000 


def max_product_of_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    # dp[i] will store the maximum product of an increasing subsequence ending at index i
    dp = [0] * n
    dp[0] = arr[0]
    max_product = arr[0]
    
    for i in range(1, n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] * arr[i])
        max_product = max(max_product, dp[i])
    return max_product

check(max_product_of_increasing_subsequence)
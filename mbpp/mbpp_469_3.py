def check(candidate):
    assert candidate([1, 5, 2, 3, 7, 6, 4, 5], 3) == 10
    assert candidate([2, 4, 7, 5, 4, 3, 5], 2) == 7
    assert candidate([10, 6, 8, 4, 2], 2) == 2


def max_profit(k, prices):
    n = len(prices)
    if n < 2 or k == 0:
        return 0
    
    # Initialize a 2D array to store maximum profit for up to i transactions
    # dp[i][j] represents the maximum profit with i transactions up to day j
    dp = [[0] * n for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        for j in range(1, n):
            # Calculate the maximum profit by either holding or selling
            # dp[i][j] = max(dp[i][j-1], prices[j] - prices[j-1] + dp[i-1][j-1])
            # But we need to track the maximum profit for the previous day
            max_diff = 0
            for m in range(1, j):
                max_diff = max(max_diff, prices[j] - prices[m] + dp[i-1][m-1])
            dp[i][j] = max(dp[i][j-1], max_diff)
    
    return dp[k][n-1]

check(max_profit)
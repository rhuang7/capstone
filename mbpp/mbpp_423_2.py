def check(candidate):
    assert candidate([[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]],4,4)==16
    assert candidate([[10,20],[30,40]],2,2)==70
    assert candidate([[4,9],[3,7]],2,2)==13


def gold_mine_problem(grid, m, n):
    # Create a DP table with dimensions (m x n)
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    # Initialize the first row
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(n):
            # Check all possible directions (up, up-left, up-right)
            max_val = 0
            if j - 1 >= 0:
                max_val = max(max_val, dp[i-1][j-1])
            if j + 1 < n:
                max_val = max(max_val, dp[i-1][j+1])
            if j >= 0:
                max_val = max(max_val, dp[i-1][j])
            dp[i][j] = grid[i][j] + max_val
    
    # Find the maximum value in the last row
    return max(dp[m-1])

check(gold_mine_problem)
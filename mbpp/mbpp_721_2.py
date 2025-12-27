def check(candidate):
    assert candidate([[1, 2, 3], [6, 5, 4], [7, 3, 9]], 3) == 5.2
    assert candidate([[2, 3, 4], [7, 6, 5], [8, 4, 10]], 3) == 6.2
    assert candidate([[3, 4, 5], [8, 7, 6], [9, 5, 11]], 3) == 7.2 


def max_average_path(matrix):
    n = len(matrix)
    # Initialize a 2D array to store the maximum average path to each cell
    dp = [[0.0 for _ in range(n)] for _ in range(n)]
    
    # Start from the top-left corner
    dp[0][0] = matrix[0][0]
    
    # Fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    
    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    
    # Fill the rest of the dp table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    # Find the maximum average path
    max_avg = max(dp[i][j] for i in range(n) for j in range(n))
    
    return max_avg

check(max_average_path)
def check(candidate):
    assert candidate([[1], [2,1], [3,3,2]], 3) == 6
    assert candidate([[1], [1, 2], [4, 1, 12]], 3) == 15 
    assert candidate([[2], [3,2], [13,23,12]], 3) == 28


def max_sum_right_triangle(triangle):
    if not triangle or not triangle[0]:
        return 0
    
    rows = len(triangle)
    cols = len(triangle[0])
    
    # Create a DP table to store maximum sum ending at each cell
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the first row
    for j in range(cols):
        dp[0][j] = triangle[0][j]
    
    # Fill the DP table
    for i in range(1, rows):
        for j in range(cols):
            # Can come from the cell above or the cell to the left
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i][j-1])
    
    # The maximum sum is the maximum value in the last row
    return max(dp[-1])

check(max_sum_right_triangle)
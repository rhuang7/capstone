def check(candidate):
    assert candidate(6) == 3
    assert candidate(2) == 2
    assert candidate(4) == 1


def min_squares_sum(n):
    # Initialize a list to store the minimum number of squares for each number up to n
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 can be formed with 0 squares

    for i in range(1, n + 1):
        # Check all possible squares less than or equal to i
        for j in range(1, int(i**0.5) + 1):
            dp[i] = min(dp[i], dp[i - j*j] + 1)

    return dp[n]

check(min_squares_sum)
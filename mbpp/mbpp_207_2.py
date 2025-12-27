def check(candidate):
    assert candidate("AABEBCDD") == 3
    assert candidate("aabb") == 2
    assert candidate("aab") == 1


def longest_repeating_subsequence(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if s[i] != s[j - 1]:
                dp[i][j] = dp[i + 1][j - 1] + 1
            else:
                dp[i][j] = dp[i + 1][j - 1]
    
    return dp[0][n]

check(longest_repeating_subsequence)
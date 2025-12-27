def check(candidate):
    assert candidate("TENS FOR TENS") == 5 
    assert candidate("CARDIO FOR CARDS") == 7
    assert candidate("PART OF THE JOURNEY IS PART") == 9 


def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

check(longest_palindromic_subsequence)
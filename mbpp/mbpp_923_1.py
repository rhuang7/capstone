def check(candidate):
    assert candidate("AGGTAB", "GXTXAYB", 6, 7) == 9
    assert candidate("feek", "eke", 4, 3) == 5
    assert candidate("PARRT", "RTA", 5, 3) == 6


def shortest_common_supersequence_length(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a table to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the shortest common supersequence is
    # (m + n - length of LCS)
    return m + n - dp[m][n]

check(shortest_common_supersequence_length)
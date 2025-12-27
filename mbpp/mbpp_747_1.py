def check(candidate):
    assert candidate('AGGT12', '12TXAYB', '12XBA', 6, 7, 5) == 2
    assert candidate('Reels', 'Reelsfor', 'ReelsforReels', 5, 8, 13) == 5 
    assert candidate('abcd1e2', 'bc12ea', 'bd1ea', 7, 6, 5) == 3


def longest_common_subsequence(s1, s2, s3):
    m, n, o = len(s1), len(s2), len(s3)
    dp = [[[-1 for _ in range(o + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif s1[i-1] == s2[j-1] == s3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )
    return dp[m][n][o]

check(longest_common_subsequence)
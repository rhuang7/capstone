def check(candidate):
    assert candidate(2) == 3
    assert candidate(8) == 153
    assert candidate(12) == 2131


def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    # dp[i] represents the number of ways to fill a 3 x i board
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
    return dp[n]

check(count_ways)
def check(candidate):
    assert candidate(7, 2) == 924
    assert candidate(3, 0) == 2
    assert candidate(3, 1) == 3


def rencontres_number(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Using dynamic programming to compute the nth rencontres number
    # The recurrence relation is: D(n) = (n-1) * (D(n-1) + D(n-2))
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
    return dp[n]

check(rencontres_number)
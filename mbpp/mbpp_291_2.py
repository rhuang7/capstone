def check(candidate):
    assert candidate(2, 4) == 16
    assert candidate(3, 2) == 6
    assert candidate(4, 4) == 228


def count_painting_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k
    
    # dp[i] represents the number of ways to paint i posts
    dp = [0] * (n + 1)
    dp[1] = k
    dp[2] = k * k
    
    for i in range(3, n + 1):
        # If the i-th post is different from the (i-1)-th post
        # Then the (i-1)-th post can be painted in (k-1) ways
        # And the i-th post can be painted in (k-1) ways
        # So total ways for this case: (k-1) * (k-1)
        # If the i-th post is same as the (i-1)-th post
        # Then the (i-2)-th post must be different from the (i-1)-th post
        # So total ways for this case: (k-1) * 1
        dp[i] = (k - 1) * (k - 1) + (k - 1) * 1
    
    return dp[n]

check(count_painting_ways)
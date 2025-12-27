def check(candidate):
    assert candidate([3, 34, 4, 12, 5, 2], 6, 9) == True
    assert candidate([3, 34, 4, 12, 5, 2], 6, 30) == False
    assert candidate([3, 34, 4, 12, 5, 2], 6, 15) == True


def subset_sum_exists(s, sum):
    n = len(s)
    dp = [False] * (sum + 1)
    dp[0] = True

    for num in s:
        for i in range(sum, num - 1, -1):
            if dp[i - num]:
                dp[i] = True

    return dp[sum]

check(subset_sum_exists)
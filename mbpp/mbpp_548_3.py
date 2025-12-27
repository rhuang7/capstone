def check(candidate):
    assert candidate([10, 22, 9, 33, 21, 50, 41, 60]) == 5
    assert candidate([3, 10, 2, 1, 20]) == 3
    assert candidate([50, 3, 10, 7, 40, 80]) == 4 


def longest_increasing_subsequence_length(sequence):
    import bisect
    dp = []
    for num in sequence:
        idx = bisect.bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
    return len(dp)

check(longest_increasing_subsequence_length)
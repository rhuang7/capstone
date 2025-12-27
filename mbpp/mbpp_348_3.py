def check(candidate):
    assert candidate(4) == 2
    assert candidate(6) == 5
    assert candidate(8) == 14


def count_valid_sequences(target_length, values):
    from collections import defaultdict

    # Initialize a dictionary to store the number of ways to reach each sum
    dp = defaultdict(int)
    dp[0] = 1  # Base case: one way to have sum 0 with 0 elements

    for _ in range(target_length):
        new_dp = defaultdict(int)
        for current_sum, count in dp.items():
            for value in values:
                new_sum = current_sum + value
                new_dp[new_sum] += count
        dp = new_dp

    # Sum all the ways to reach a non-negative sum at the end
    return sum(dp[sum_val] for sum_val in dp if sum_val >= 0)

check(count_valid_sequences)
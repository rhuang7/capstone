def check(candidate):
    assert candidate([1, 2, 3],3,4)==4
    assert candidate([4,5,6,7,8,9],6,9)==2
    assert candidate([4,5,6,7,8,9],6,4)==1


def count_coin_change(amount, coins):
    """
    Returns the number of ways to make a given amount using specified coin denominations.
    """
    # Initialize a dp array where dp[i] represents the number of ways to make amount i
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is 1 way to make amount 0: use no coins

    # Iterate over each coin denomination
    for coin in coins:
        # Update the dp array for all amounts from coin to amount
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

check(count_coin_change)
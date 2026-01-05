import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    activities = list(map(int, data[1:N+1]))
    
    if N == 0:
        print(0)
        return
    
    # dp[i] = minimum total minutes for first i days
    dp = [0] * (N + 1)
    # dp[i] can be computed based on the previous 3 days
    # We need to track the last 3 days' choices
    # So we use a sliding window of the last 3 days' values
    # We'll use a list to store the last 3 days' values
    # We'll also use a list to store the minimum total minutes for the last 3 days
    # Initialize the first 3 days
    dp[0] = 0
    dp[1] = activities[0]
    dp[2] = activities[0] + activities[1]
    dp[3] = activities[0] + activities[1] + activities[2]
    
    for i in range(4, N + 1):
        # We can take the previous 3 days' minimum and add the current day's activity
        # But we need to make sure that we don't take 3 consecutive days
        # So we look at the last 3 days' minimum and add the current day's activity
        # We can take the minimum of the last 3 days' values
        # But we need to make sure that we don't take 3 consecutive days
        # So we look at the last 3 days' minimum and add the current day's activity
        # We can take the minimum of the last 3 days' values
        # But we need to make sure that we don't take 3 consecutive days
        # So we look at the last 3 days' minimum and add the current day's activity
        # We can take the minimum of the last 3 days' values
        # But we need to make sure that we don't take 3 consecutive days
        # So we look at the last 3 days' minimum and add the current day's activity
        dp[i] = min(dp[i-1], dp[i-2], dp[i-3]) + activities[i-1]
    
    print(dp[N])

if __name__ == '__main__':
    solve()
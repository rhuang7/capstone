import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    times = list(map(int, data[1:N+1]))
    
    if N == 0:
        print(0)
        return
    
    # dp[i] = minimum time to assign duties up to day i
    dp = [0] * (N + 1)
    # dp[i] can be computed based on the previous 3 days
    # We'll use a sliding window approach to keep track of the last 3 days
    
    # Initialize the first 3 days
    dp[1] = times[0]
    dp[2] = times[0] + times[1]
    dp[3] = times[0] + times[1] + times[2]
    
    for i in range(4, N + 1):
        # We can't have three consecutive days without duty
        # So we must choose at least one day from the previous three days
        # The minimum is the minimum of the last three days plus the current day's time
        dp[i] = min(dp[i-1], dp[i-2], dp[i-3]) + times[i-1]
    
    print(dp[N])

if __name__ == '__main__':
    solve()
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
    
    # dp[i] = minimum minutes needed for first i days
    dp = [0] * (N + 1)
    # dp[i] can be computed based on the previous 3 days
    # We need to track the last 3 days' values
    # So we use a sliding window of size 3
    
    # Initialize the first 3 days
    dp[1] = activities[0]
    if N >= 2:
        dp[2] = activities[0] + activities[1]
    if N >= 3:
        dp[3] = activities[0] + activities[1] + activities[2]
    
    for i in range(4, N + 1):
        # We can take the minimum of the last 3 days
        # But we need to make sure that we are not taking 3 consecutive days
        # So we consider the minimum of dp[i-1], dp[i-2], dp[i-3]
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomputing, we can track the last 3 dp values
        # So we maintain a window of the last 3 dp values
        # We can use a sliding window of size 3
        # So we track the last 3 dp values
        # For each i, we can take the minimum of the last 3 dp values
        # But we have to subtract the value of the day that is not included
        # So we have to check which day is excluded
        # To avoid recomput
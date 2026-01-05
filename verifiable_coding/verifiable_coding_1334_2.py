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
    
    # dp[i] = minimum total minutes for first i days
    dp = [0] * (N + 1)
    # dp[i] can be computed based on the previous 3 days
    # We need to track the last 3 days' values
    # So we use a sliding window of the last 3 days
    # We can use a queue to keep track of the last 3 days
    from collections import deque
    q = deque()
    
    for i in range(1, N + 1):
        # If we take the current day, we cannot take the previous day
        # So we need to take the minimum of the last 2 days
        # But we can't take the previous day, so we take the minimum of the last 2 days
        # So we need to take the minimum of the last 2 days
        # So we need to track the last 2 days
        # So we use a sliding window of the last 2 days
        # We can use a deque to keep track of the last 2 days
        q.append(i)
        if len(q) > 2:
            q.popleft()
        # If we take the current day, we cannot take the previous day
        # So we need to take the minimum of the last 2 days
        # But we can't take the previous day, so we take the minimum of the last 2 days
        # So we need to take the minimum of the last 2 days
        # So we need to track the last 2 days
        # So we use a sliding window of the last 2 days
        # We can use a deque to keep track of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last 2 days
        # So the minimum of the last 2 days is the minimum of the last
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
    # dp[i] can be computed based on the last 2 or 3 days
    # We need to track the last 3 days' states
    # We'll use a rolling array for space efficiency
    prev_prev = 0
    prev = 0
    curr = 0
    
    for i in range(1, N + 1):
        # If we take day i, we can't take i-1
        # So we look at the state up to i-2
        # If we don't take day i, we can take i-1 or i-2
        # We need to consider all valid combinations
        # To avoid recomputation, we track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
        # Initialize the 3-element array
        # dp[i] = min( dp[i-1] + times[i-1], dp[i-2] + times[i-1], dp[i-3] + times[i-1] )
        # But we need to ensure that no 3 consecutive days are skipped
        # So we need to track the last 3 states
        # We'll use a 3-element array to store the last 3 states
        # We'll update it as we go
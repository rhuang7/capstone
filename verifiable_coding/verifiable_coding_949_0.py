import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each position i, find the maximum number of moves starting from i
        # We'll use dynamic programming
        dp = [0] * N
        # For each position i, we can move to i+1 or i+2 if the value is the same
        # So we'll iterate from the end to the beginning
        for i in range(N-1, -1, -1):
            # Check if we can move to i+1
            if i + 1 < N and a[i] == a[i+1]:
                dp[i] = max(dp[i], dp[i+1] + 1)
            # Check if we can move to i+2
            if i + 2 < N and a[i] == a[i+2]:
                dp[i] = max(dp[i], dp[i+2] + 1)
        
        # The maximum number of moves is the maximum value in dp
        results.append(str(max(dp)))
    
    print('\n'.join(results))
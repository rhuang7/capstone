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
        # We can use dynamic programming
        dp = [0] * N
        # We'll process from right to left
        for i in range(N-2, -1, -1):
            # Check if we can move 1 step forward
            if a[i] == a[i+1]:
                dp[i] = dp[i+1] + 1
            # Check if we can move 2 steps forward
            if i + 1 < N and a[i] == a[i+2]:
                dp[i] = max(dp[i], dp[i+2] + 1)
        
        # The answer is the maximum value in dp
        results.append(str(max(dp)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
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
        
        # For each position, find the maximum number of moves
        # We can use BFS for each position, but that would be too slow
        # Instead, we can use dynamic programming
        
        # dp[i] = maximum number of moves starting from position i
        dp = [0] * N
        
        # We'll process from the end to the beginning
        for i in range(N-2, -1, -1):
            x = a[i]
            # Check if we can move 1 step
            if i + 1 < N and a[i+1] == x:
                dp[i] = dp[i+1] + 1
            # Check if we can move 2 steps
            if i + 2 < N and a[i+2] == x:
                dp[i] = max(dp[i], dp[i+2] + 1)
        
        results.append(max(dp))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
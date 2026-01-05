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
        
        # For each position, find the maximum number of moves starting from that position
        # We can use BFS or dynamic programming
        # Since the graph is directed and has edges of length 1 and 2, we can use dynamic programming
        
        # dp[i] = maximum number of moves starting from position i
        dp = [0] * N
        
        # We process from the end to the beginning
        for i in range(N-2, -1, -1):
            # Check if we can move 1 step forward
            if a[i] == a[i+1]:
                dp[i] = max(dp[i], 1 + dp[i+1])
            # Check if we can move 2 steps forward
            if i + 1 < N and a[i] == a[i+2]:
                dp[i] = max(dp[i], 1 + dp[i+2])
        
        # The answer is the maximum value in dp
        results.append(max(dp))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
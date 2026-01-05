import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We need to determine if Vanja can force the absolute value of the expression to be >= K
        # Since the players alternate and Vanja starts, we can model this with dynamic programming
        # Let dp[i][v] be True if the current player can force the absolute value to be >= K
        # We use a memoization approach with recursion and memoization
        
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, val):
            if i == N:
                return abs(val) >= K
            # Current player can choose + or -
            return dfs(i + 1, val + A[i]) or dfs(i + 1, val - A[i])
        
        if dfs(0, 0):
            results.append(1)
        else:
            results.append(2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
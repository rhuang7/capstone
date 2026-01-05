```python
import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    
    # dp[i][j] represents the number of non-increasing arrays of length i
    # ending with value j
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    
    # Base case: arrays of length 1
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # Fill the DP table
    for i in range(2, K + 1):
        for j in range(1, N + 1):
            # Sum of all ways to have arrays of length i-1 ending with values >= j
            for k in range(j, N + 1):
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD
    
    # Sum all possibilities for arrays of length K
    result = sum(dp[K][j] for j in range(1, N + 1)) % MOD
    print(result)

if __name__ == '__main__':
    solve()
```
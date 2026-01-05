import sys
import math

MOD = 10**9

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        
        if N == 1:
            results.append((M + 1) % MOD)
            continue
        
        # Precompute factorials and inverse factorials modulo MOD
        max_n = N * M
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # dp[i][j] = number of ways to have sum j in the i-th row
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        
        for i in range(1, N + 1):
            for j in range(M + 1):
                if i == 1:
                    dp[i][j] = (dp[i-1][j] * (M + 1)) % MOD
                else:
                    for k in range(j + 1):
                        dp[i][j] = (dp[i][j] + dp[i-1][k] * (M + 1 - k)) % MOD
        
        ans = 0
        for j in range(M + 1):
            ans = (ans + dp[N][j]) % MOD
        
        results.append(ans % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
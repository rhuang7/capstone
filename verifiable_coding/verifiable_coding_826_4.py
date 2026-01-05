import sys
MOD = 10**9

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        
        # Precompute factorials and inverse factorials modulo MOD
        max_n = N * M
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # Function to compute combination C(n, k) mod MOD
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        
        # Dynamic programming to compute the number of steady tables
        # dp[i][j] = number of ways to fill the first i rows with sum j
        dp = [ [0] * (M + 1) for _ in range(N + 1) ]
        dp[0][0] = 1
        
        for i in range(1, N + 1):
            for j in range(M + 1):
                # The sum of the i-th row must be at least the sum of the (i-1)-th row
                # So we need to consider all possible sums for the i-th row that are >= previous sum
                for k in range(j, M + 1):
                    dp[i][k] = (dp[i][k] + dp[i-1][j] * comb(k, j)) % MOD
        
        # The last row's sum must be <= M
        ans = sum(dp[N][j] for j in range(M + 1)) % MOD
        results.append(ans)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
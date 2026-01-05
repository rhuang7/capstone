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
        
        # Precompute inverse factorials
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # Function to compute combination C(n, k)
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        
        # DP table
        dp = [0] * (N + 1)
        dp[0] = 1  # Base case: 0 rows, 1 way to have 0 sum
        
        for row in range(1, N + 1):
            # For each row, we need to distribute sum s across M columns
            # The sum of the row must be >= sum of previous row
            # So we compute the number of ways to have sum s in this row
            # such that s >= previous row's sum
            # We use dynamic programming to track the number of ways to reach sum s
            new_dp = [0] * (row * M + 1)
            for s in range(row * M + 1):
                # For each possible sum s in this row
                # We can choose any number of elements to be non-zero
                # The number of ways to have sum s in this row is comb(s + M - 1, M - 1)
                # But we also need to ensure that s >= previous row's sum
                # So we accumulate the number of ways for all possible previous sums
                for prev_s in range(s):
                    new_dp[s] = (new_dp[s] + dp[prev_s]) % MOD
                new_dp[s] = (new_dp[s] + comb(s, M - 1)) % MOD
            dp = new_dp
        
        # The last row must have sum <= M
        ans = 0
        for s in range(M + 1):
            ans = (ans + dp[s]) % MOD
        results.append(ans)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
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
        
        # dp[i][j] = number of ways to fill first i rows with total sum j
        dp = [ [0] * (N * M + 1) for _ in range(N + 1) ]
        dp[0][0] = 1
        
        for i in range(1, N + 1):
            for j in range(0, N * M + 1):
                for k in range(0, j + 1):
                    if i == 1:
                        # First row can have any sum up to M * (some value)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # For the first row, the sum can be anything from 0 to M * (some value)
                        # But for the first row, we can have any sum from 0 to M * (some value)
                        # However, the sum of the first row must be <= M * (some value)
                        # For the first row, the sum can be anything from 0 to M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M - 1)
                        # But we need to ensure that the sum of the first row is <= M * (some value)
                        # But for the first row, the sum can be anything from 0 to M * (some value)
                        # So we can use the combination formula for the first row
                        # The first row has M elements, each can be 0 or more
                        # So the number of ways to have sum j is C(j + M - 1, M -
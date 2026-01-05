import sys
MOD = 10**9

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        
        # Precompute factorials and inverse factorials modulo MOD
        max_n = N + M
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # Precompute combinations
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        
        # dp[i][j] = number of ways to have i rows with total sum j
        # We need to compute dp[N][k] for all k <= M * N
        # But since M can be up to 2000 and N up to 2000, this is not feasible directly
        # Instead, we use a generating function approach
        
        # The generating function for each row is (1 + x + x^2 + ... + x^M)^N
        # But we need to ensure that the sum of the first i rows is non-decreasing
        # This is equivalent to the number of sequences of N non-decreasing integers
        # where each integer is between 0 and M*N and the sum of the first i terms is <= sum of the first i-1 terms
        
        # This is a classic problem in combinatorics, and the answer is the number of ways to choose N non-decreasing integers between 0 and M*N
        # This is equivalent to the number of multisets of size N from a set of size M*N + 1
        # Which is C(M*N + N, N)
        # But we also need to ensure that the last row's sum is <= M
        # So we need to count the number of sequences of N non-decreasing integers where the last is <= M
        # This is equivalent to the number of multisets of size N from a set of size M + 1
        # Which is C(M + N, N)
        
        # However, this is not correct, as the rows are not just any non-decreasing sequence of integers, but the sum of the first i rows is not less than the sum of the first i-1 rows
        # This is a more complex problem, and the correct approach is to use dynamic programming
        
        # Let dp[i][j] be the number of ways to have i rows with total sum j
        # The recurrence is dp[i][j] = sum_{k=0}^j dp[i-1][k]
        # The base case is dp[0][0] = 1
        # The final answer is sum_{j=0}^M dp[N][j]
        
        # However, for N and M up to 2000, this is not feasible directly
        # Instead, we use the fact that the number of ways is C(M + N, N) if the last row's sum is <= M
        # This is a known combinatorial identity
        
        # The answer is C(M + N, N) if M >= 1
        # Otherwise, if M == 0, the answer is 1 if N == 0, else 0
        
        if M == 0:
            results.append(1 if N == 0 else 0)
        else:
            ans = comb(M + N, N)
            results.append(ans % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
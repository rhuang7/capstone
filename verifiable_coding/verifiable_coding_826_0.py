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
        
        # Base case: if N=1, the answer is (M+1) choose M
        if N == 1:
            res = (M + 1) * (M + 2) // 2
            results.append(res % MOD)
            continue
        
        # For N >= 2, the answer is (M + 1) choose (M + N - 1) - (M + 1) choose (M + N)
        # We use combinatorial identities and precompute factorials and inverse factorials
        # Precompute factorials and inverse factorials up to 4000 (since M + N can be up to 4000)
        max_n = 4000
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        
        a = comb(M + N - 1, M)
        b = comb(M + N, M)
        res = (a - b) % MOD
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
import sys
MOD = 10**9 + 7

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
        S = data[idx + 1]
        idx += 2
        
        len_S = len(S)
        
        if N < len_S:
            results.append(0)
            continue
        
        # Number of ways to insert len_S characters into N positions
        # = C(N, len_S) * 26^len_S
        # But we need to compute it modulo 1e9+7
        
        # Precompute factorials and inverse factorials up to 1e5
        # Since len_S can be up to 1e5, and N can be up to 1e18, we need to compute combinations
        # using modular inverses and precomputed factorials
        
        # Precompute factorials and inverse factorials up to 1e5
        max_fact = 10**5
        fact = [1] * (max_fact + 1)
        inv_fact = [1] * (max_fact + 1)
        
        for i in range(1, max_fact + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        inv_fact[max_fact] = pow(fact[max_fact], MOD - 2, MOD)
        for i in range(max_fact - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        # Compute combination C(N, len_S) mod MOD
        # Since N can be up to 1e18, we need to compute it using Lucas theorem
        # But for the purpose of this problem, we can use the fact that len_S is up to 1e5
        # and N can be very large, but we can compute C(N, len_S) using the formula:
        # C(N, k) = N * (N - 1) * ... * (N - k + 1) / k!
        
        k = len_S
        if k == 0:
            results.append(1)
            continue
        
        numerator = 1
        for i in range(k):
            numerator = numerator * (N - i) % MOD
        
        comb = numerator * inv_fact[k] % MOD
        
        # Compute 26^k mod MOD
        power_26 = pow(26, k, MOD)
        
        ans = comb * power_26 % MOD
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
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
        idx += 1
        maxnumbers = list(map(int, data[idx:idx+N]))
        idx += N
        
        maxnumbers.sort()
        max_val = maxnumbers[-1]
        
        # Check if it's possible to assign distinct numbers
        if max_val < N:
            results.append(0)
            continue
        
        # Precompute factorials and inverse factorials modulo MOD
        fact = [1] * (max_val + 1)
        for i in range(1, max_val + 1):
            fact[i] = fact[i-1] * i % MOD
        
        # Precompute inverse factorials
        inv_fact = [1] * (max_val + 1)
        inv_fact[max_val] = pow(fact[max_val], MOD-2, MOD)
        for i in range(max_val-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # Compute the answer using permutation formula
        ans = 0
        for i in range(N):
            # Number of choices for the i-th person
            # It's (maxnumbers[i] - i) because we need to choose a number not used before
            # So we choose (maxnumbers[i] - i) numbers from (maxnumbers[i] - i) available
            # and multiply by the permutation of (maxnumbers[i] - i) taken (i+1) at a time
            # But we need to check if (maxnumbers[i] - i) >= (i+1)
            if maxnumbers[i] - i < i + 1:
                break
            # The number of ways is (maxnumbers[i] - i) choose (i+1) multiplied by (i+1)! / (maxnumbers[i] - i - (i+1))! )
            # Which is (maxnumbers[i] - i) * (maxnumbers[i] - i - 1) * ... * (maxnumbers[i] - i - (i+1) + 1)
            # So it's the product of (maxnumbers[i] - i - k) for k in 0 to i
            # Which is fact[maxnumbers[i] - i] * inv_fact[maxnumbers[i] - i - (i+1)] 
            # But since maxnumbers[i] - i - (i+1) = maxnumbers[i] - 2i - 1
            # So we need to compute fact[maxnumbers[i] - i] * inv_fact[maxnumbers[i] - 2i - 1]
            # But if maxnumbers[i] - 2i - 1 < 0, it's invalid
            # So we need to compute the product of (maxnumbers[i] - i - k) for k in 0 to i
            # Which is the same as fact[maxnumbers[i] - i] // fact[maxnumbers[i] - i - (i+1)]
            # Which is fact[maxnumbers[i] - i] * inv_fact[maxnumbers[i] - i - (i+1)] mod MOD
            # So we compute fact[maxnumbers[i] - i] * inv_fact[maxnumbers[i] - 2i - 1] mod MOD
            # But if maxnumbers[i] - 2i - 1 < 0, it's invalid
            # So we need to check if maxnumbers[i] - i >= i + 1
            # Which is equivalent to maxnumbers[i] >= 2i + 1
            # So if maxnumbers[i] < 2i + 1, it's invalid
            # So we can break early
            if maxnumbers[i] < 2 * i + 1:
                break
            # Compute the product of (maxnumbers[i] - i - k) for k in 0 to i
            # Which is fact[maxnumbers[i] - i] * inv_fact[maxnumbers[i] - i - (i+1)] mod MOD
            # Which is fact[maxnumbers[i] - i] * inv_fact[maxnumbers[i] - 2i - 1] mod MOD
            # So we compute this
            term = fact[maxnumbers[i] - i] * inv_fact[maxnumbers[i] - 2 * i - 1] % MOD
            ans = (ans + term) % MOD
        
        results.append(ans)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
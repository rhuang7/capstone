import sys
import math

MOD = 998244353

def main():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        x1 = int(data[idx+2])
        y1 = int(data[idx+3])
        x2 = int(data[idx+4])
        y2 = int(data[idx+5])
        idx += 6
        
        # Precompute factorials and inverse factorials up to 2e5
        max_n = n + m
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        def comb(a, b):
            if a < 0 or b < 0 or a < b:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        
        # Total paths from (0,0) to (n,m)
        total = comb(n + m, n)
        
        # Paths passing through X
        paths_through_x = comb(n + m, n - x1 + y1) * comb(x1 + y1, x1) % MOD
        paths_through_x = paths_through_x * comb(n - x1 + m - y1, n - x1) % MOD
        
        # Paths passing through Y
        paths_through_y = comb(n + m, n - x2 + y2) * comb(x2 + y2, x2) % MOD
        paths_through_y = paths_through_y * comb(n - x2 + m - y2, n - x2) % MOD
        
        # Paths passing through both X and Y
        # Check if X is before Y in path
        if x1 <= x2 and y1 <= y2:
            paths_through_both = comb(n + m, n - x1 + y1) * comb(x1 + y1, x1) % MOD
            paths_through_both = paths_through_both * comb(n - x1 + m - y1, n - x1 + m - y1 - (x2 - x1) - (y2 - y1)) % MOD
            paths_through_both = paths_through_both * comb(x2 + y2, x2) % MOD
            paths_through_both = paths_through_both * comb(n - x2 + m - y2, n - x2) % MOD
        else:
            paths_through_both = 0
        
        # Inclusion-exclusion principle
        ans = (total - paths_through_x - paths_through_y + paths_through_both) % MOD
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()
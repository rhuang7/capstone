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
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        def comb(a, b):
            if a < 0 or b < 0 or a < b:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        
        # Total ways from (0,0) to (n,m)
        total = comb(n + m, n)
        
        # Ways passing through X
        ways_x = comb(n + m, n - x1 + y1) * comb(x1 + y1, x1) % MOD
        ways_x = ways_x * comb(n - x1 + m - y1, n - x1) % MOD
        
        # Ways passing through Y
        ways_y = comb(n + m, n - x2 + y2) * comb(x2 + y2, x2) % MOD
        ways_y = ways_y * comb(n - x2 + m - y2, n - x2) % MOD
        
        # Ways passing through both X and Y
        # Check if X is before Y
        if x1 <= x2 and y1 <= y2:
            ways_xy = comb(n + m, n - x1 + y1) * comb(x1 + y1, x1) % MOD
            ways_xy = ways_xy * comb(n - x1 + m - y1, n - x1 + x2 - x1 + y2 - y1) % MOD
            ways_xy = ways_xy * comb(x2 + y2, x2) % MOD
            ways_xy = ways_xy * comb(n - x2 + m - y2, n - x2) % MOD
        else:
            ways_xy = 0
        
        # Inclusion-exclusion principle
        result = (total - ways_x - ways_y + ways_xy) % MOD
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()
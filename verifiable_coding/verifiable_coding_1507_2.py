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
        
        total = comb(n + m, n)
        # Subtract paths passing through X or Y
        # Add back paths passing through both X and Y (inclusion-exclusion)
        pass_x = comb(n + m, x1 + y1) * comb(n - x1 + m - y1, n - x1) % MOD
        pass_y = comb(n + m, x2 + y2) * comb(n - x2 + m - y2, n - x2) % MOD
        pass_xy = comb(n + m, x1 + y1) * comb(n - x1 + m - y1, x2 - x1 + y2 - y1) % MOD * comb(n - x2 + m - y2, n - x2) % MOD
        
        ans = (total - pass_x - pass_y + pass_xy) % MOD
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()
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
        
        # Precompute factorials and inverse factorials modulo MOD
        # Since n and m can be up to 1e5, we precompute up to 2e5
        max_n = 2 * 10**5 + 10
        fact = [1] * (max_n)
        inv_fact = [1] * (max_n)
        for i in range(1, max_n):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[max_n-1] = pow(fact[max_n-1], MOD-2, MOD)
        for i in range(max_n-2, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        def comb(a, b):
            if a < 0 or b < 0 or a < b:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        
        # Total ways from (0,0) to (n,m)
        total = comb(n + m, n)
        
        # Ways passing through X
        ways_x = comb(x1 + y1, x1) * comb(n - x1 + m - y1, n - x1) % MOD
        
        # Ways passing through Y
        ways_y = comb(x2 + y2, x2) * comb(n - x2 + m - y2, n - x2) % MOD
        
        # Ways passing through both X and Y
        # Check if X is before Y in the path
        if x1 <= x2 and y1 <= y2:
            ways_xy = comb(x1 + y1, x1) * comb(x2 - x1 + y2 - y1, x2 - x1) % MOD
            ways_xy = ways_xy * comb(n - x2 + m - y2, n - x2) % MOD
        else:
            ways_xy = 0
        
        # Inclusion-exclusion principle
        ans = (total - ways_x - ways_y + ways_xy) % MOD
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()
import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx+1])
        idx += 2
        
        # Precompute powers of 2 up to 60 (since 2^60 is larger than 1e18)
        pow2 = [1] * 61
        for i in range(1, 61):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        # Function to compute the bitwise AND of numbers from a to b
        def and_range(a, b):
            res = a
            for i in range(a+1, b+1):
                res &= i
            return res
        
        # Precompute the AND values for all ranges [L, i] for i from L to R
        # But since L and R can be up to 1e18, we need a smarter way
        
        # Instead, we can find the pattern of the AND operation
        # The AND of a range [L, i] will eventually become 0 once a bit is cleared
        # So we can find the position where the AND becomes 0 and compute the sum accordingly
        
        # Find the position where the AND becomes 0
        pos = 0
        while (1 << pos) <= R:
            if (L & (1 << pos)) == 0:
                break
            pos += 1
        
        # The AND of [L, i] will be 0 for i >= (L | (1 << pos))
        # So we can split the sum into two parts:
        # 1. From L to (L | (1 << pos)) - 1
        # 2. From (L | (1 << pos)) to R
        
        # Compute the sum for the first part
        sum1 = 0
        for i in range(L, (L | (1 << pos))):
            and_val = and_range(L, i)
            sum1 = (sum1 + and_val) % MOD
        
        # Compute the sum for the second part
        sum2 = 0
        for i in range((L | (1 << pos)), R + 1):
            and_val = and_range(L, i)
            sum2 = (sum2 + and_val) % MOD
        
        total = (sum1 + sum2) % MOD
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()